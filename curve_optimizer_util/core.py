from typing import List


class Core:
    def __init__(
        self,
        total_num: int,
        index: int = None,
        friendly_number: int = None,
        hyper_threading: bool = True,
    ):
        """
        total_num is total number of threads.
        index is zero-indexed thread index
        friendly_number is 1-indexed thread index
        """
        if index is None and friendly_number is None:
            raise ValueError(
                "One of index, friendly_number must be" " provided as an int"
            )
        if (
            (index is not None)
            and (friendly_number is not None)
            and (friendly_number != index + 1)
        ):
            raise ValueError("index must be 1 lower than friendly_number")

        self.total_num = total_num

        if index is not None:
            self.index = index
            self.friendly_number = index + 1
        else:
            self.friendly_number = friendly_number
            self.index = friendly_number - 1

        self.hyper_threading = hyper_threading

    def __repr__(self):
        return (
            f"Core {self._handle_padding()}" f"{self.friendly_number}/{self.total_num}"
        )

    def _handle_padding(self) -> str:
        if self.total_num >= 10 and self.friendly_number < 10:
            return " "
        return ""

    @property
    def affinity_mask(self):
        index = self.index * (int(self.hyper_threading) + 1)
        return {index, index + int(self.hyper_threading)}


def get_cores(hyper_threading: bool, core_num: int) -> List[Core]:
    return [
        Core(core_num, index=n, hyper_threading=hyper_threading)
        for n in range(core_num)
    ]
