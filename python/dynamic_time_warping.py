# -*- coding: utf-8 -*-

from typing import List
from typing import Sequence
from typing import Tuple

Matrix = List[List[int]]


def get_cost_matrix(seq1: Sequence[int], seq2: Sequence[int]) -> Matrix:
    cost_matrix = [[0 for _ in seq1] for _ in seq2]

    for x2, elem2 in enumerate(seq2):
        for x1, elem1 in enumerate(seq1):
            if x2 == 0 and x1 == 0:
                penalty = 0
            elif x2 == 0:
                penalty = cost_matrix[0][x1 - 1]
            elif x1 == 0:
                penalty = cost_matrix[x2 - 1][0]
            else:
                penalty = min(cost_matrix[x2][x1 - 1],
                              cost_matrix[x2 - 1][x1 - 1],
                              cost_matrix[x2 - 1][x1])
            cost_matrix[x2][x1] = abs(elem1 - elem2) + penalty

    return cost_matrix


def get_optimal_path(
        cost_matrix: Matrix
) -> Tuple[Sequence[Tuple[int, int]], Sequence[int]]:
    optimal_path_pairs, optimal_path_costs = [], []
    y2, y1 = len(cost_matrix) - 1, len(cost_matrix[0]) - 1

    while True:
        optimal_path_pairs.append((y1, y2))
        optimal_path_costs.append(cost_matrix[y2][y1])
        if y1 == 0 and y2 == 0:
            break
        elif y1 == 0:
            y2 -= 1
        elif y2 == 0:
            y1 -= 1
        else:
            horizontal_cost = cost_matrix[y2][y1 - 1]
            diagonal_cost = cost_matrix[y2 - 1][y1 - 1]
            vertical_cost = cost_matrix[y2 - 1][y1]
            if horizontal_cost < diagonal_cost:
                if horizontal_cost < vertical_cost:
                    y1 -= 1
                else:
                    y2 -= 1
            else:
                y2 -= 1
                if diagonal_cost <= vertical_cost:
                    y1 -= 1

    return optimal_path_pairs[::-1], optimal_path_costs[::-1]


def run(
    seq1: Sequence[int], seq2: Sequence[int]
) -> Tuple[Sequence[Tuple[int, int]], Sequence[int], Matrix]:
    cost_matrix = get_cost_matrix(seq1, seq2)
    optimal_path_pairs, optimal_path_costs = get_optimal_path(cost_matrix)
    return optimal_path_pairs, optimal_path_costs, cost_matrix