#!/usr/bin/env python3


def get_cpuinfo() -> dict:
    with open("/proc/cpuinfo") as file_handler:
        cpuinfo = []
        temp_dict = {}
        for line in file_handler:
            try:
                key, value = map(str.strip, line.split(":", 1))
            except ValueError:
                if temp_dict:
                    cpuinfo.append(temp_dict)
                temp_dict = {}
            else:
                temp_dict[key] = value

    return cpuinfo


def is_hyperthreading_enabled() -> bool:
    cpuinfo = get_cpuinfo()

    all_cores_hyperthreaded = all(
        map(lambda core: core["siblings"] != core["cpu cores"], cpuinfo)
    )
    any_cores_hyperthreaded = any(
        map(lambda core: core["siblings"] != core["cpu cores"], cpuinfo)
    )

    if all_cores_hyperthreaded != any_cores_hyperthreaded:
        raise RuntimeError(
            "Not all cores have hyperthreading enabled. Unable to continue..."
        )

    return all_cores_hyperthreaded


def cpu_core_count() -> int:
    cpuinfo = get_cpuinfo()

    return int(cpuinfo[0]["cpu cores"])
