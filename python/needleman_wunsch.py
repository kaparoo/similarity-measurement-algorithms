# -*- coding: utf-8 -*-

from typing import List
from typing import Sequence
from typing import Tuple

Matrix = List[List[int]]


def get_cost_matrix(seq1: Sequence[int],
                    seq2: Sequence[int]) -> Tuple[Matrix, Matrix]:
    cost_matrix = [[0 for _ in seq2] for _ in seq1]
    dir_matrix = [[0 for _ in seq2] for _ in seq1]

    for y, elem2 in enumerate(seq2):
        for x, elem1 in enumerate(seq1):
            move_from = 0  # 0: diagonal, 1: vertical, -1: horizontal
            if x == 0 and y == 0:
                pass
            elif x == 0:
                pass
            elif y == 0:
                pass
            else:
                pass
            cost_matrix[y][x] = None
            dir_matrix[y][x] = None

    return cost_matrix, dir_matrix


def get_optimal_path(
        cost_matrix: Matrix,
        dir_matrix: Matrix) -> Tuple[Sequence[Tuple[int, int]], Sequence[int]]:
    pass


def run(
    seq1: Sequence[int], seq2: Sequence[int]
) -> Tuple[Sequence[Tuple[int, int]], Sequence[int], Matrix]:
    pass