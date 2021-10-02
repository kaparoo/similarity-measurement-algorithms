# -*- coding: utf-8 -*-

import copy
import math
from typing import Sequence


def display_matrix(matrix: Sequence[Sequence[int]]) -> None:
    matrix = copy.deepcopy(matrix)[::-1]
    num_digits = int(math.log10(max(map(max, matrix)))) + 1
    for raw in matrix:
        for elem in raw:
            print(f"[{elem: >{num_digits}d}]", end=" ")
        print()  # New line


if __name__ == "__main__":
    matrix = [[i * j for i in range(1, 9 + 1)] for j in range(1, 9 + 1)]
    display_matrix(matrix)