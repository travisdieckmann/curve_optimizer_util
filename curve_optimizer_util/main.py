#!/usr/bin/env python3

import os
import time
from datetime import datetime as dt, timedelta
from typing import Dict, Iterable, List

from mprime import MPrime, CONFIGURATIONS, Worker
from .cpu_details import is_hyperthreading_enabled, cpu_core_count
from .log import format_date_time, log
from .core import Core, get_cores
from .timing import wait_and_sync


def main():
    starting_core_friendly_number = 1
    log_with_date("Starting single-core stress-testing...")

    cores = get_cores(is_hyperthreading_enabled(), cpu_core_count())

    config = CONFIGURATIONS.SMALL_FFTS
    config["TortureThreads"] = int(is_hyperthreading_enabled()) + 1

    log_with_date(
        f"Discovered {len(cores)} cores with hyperthreading enabled: {is_hyperthreading_enabled()}"
    )

    mprime = MPrime(prime_config=config)
    # mprime.handlers["on_test_start"] = worker_started_handler
    mprime.handlers["on_worker_fail"] = lambda w: log_with_date(f"CRASHED: {w.status}")
    mprime.handlers["on_uncaught_output"] = lambda w: log_with_date(
        f"Uncaught Output: {w}"
    )
    mprime.handlers["on_test_complete"] = lambda w: log_with_date(
        "worker {}: {}".format(w.number, w.summary)
    )
    # mprime.handlers["on_test_start"] = lambda w: log_with_date(
    #     "worker {}: pid:{} test {}".format(w.number, w.pid, len(w.tests))
    # )
    log_with_date("Configured mprime")

    mprime.launch_mprime()
    log_with_date("Launched mprime")

    time.sleep(0.1)

    try:
        while mprime.running:
            for core in get_infinite_core_iterator(
                cores, starting_core_friendly_number
            ):
                set_active_core_for(core, mprime.workers)
                log_starting_core(core)
                wait_and_sync(timedelta(minutes=5), "True")
    except KeyboardInterrupt:
        print("Stopped")
    mprime.stop()

    log_with_date(f"Ended single-core stress-testing...")


def log_with_date(message: str):
    log(f"{format_date_time(dt.now())} {message}")


def log_starting_core(core: Core):
    log_with_date(f"switching to {core}")


def get_infinite_core_iterator(
    cores: List[Core], starting_core_friendly_number: int
) -> Iterable[Core]:
    starting_index = get_index_of_core_in(starting_core_friendly_number, cores)
    return get_infinite_iterator(cores, starting_index)


def get_index_of_core_in(friendly_number: int, cores: List[Core]) -> int:
    try:
        the_core = get_the_core_with(friendly_number, cores)
        return cores.index(the_core)
    except StopIteration:
        raise ValueError(
            "starting core number should be one of core numbers:"
            f"{list(map(lambda x: x.friendly_number, cores))}"
        )


def get_the_core_with(friendly_number: int, cores: List[Core]) -> Core:
    def is_core_with_number(core: Core):
        return core.friendly_number == friendly_number

    return next(filter(is_core_with_number, cores))


def get_infinite_iterator(collection: list, starting_index: int) -> Iterable:
    length = len(collection)
    i = starting_index
    while True:
        if i >= length:
            i = 0
        yield collection[i]
        i += 1


def set_active_core_for(core: Core, workers: Dict[int, Worker]) -> None:
    for worker_number in workers:
        os.sched_setaffinity(workers[worker_number].pid, core.affinity_mask)


if __name__ == "__main__":
    main()
