# -*- coding: utf-8 -*-

from typing import List
from typing import Sequence
from typing import Tuple

Matrix = List[List[int]]


def get_cost_matrix(seq1: Sequence[int], seq2: Sequence[int]) -> Matrix:
    cost_matrix = [[0 for _ in seq1] for _ in seq2]

    for y, elem2 in enumerate(seq2):
        for x, elem1 in enumerate(seq1):
            if y == 0 and x == 0:
                penalty = 0
            elif y == 0:
                penalty = cost_matrix[0][x - 1]
            elif x == 0:
                penalty = cost_matrix[y - 1][0]
            else:
                penalty = min(cost_matrix[y][x - 1], cost_matrix[y - 1][x - 1],
                              cost_matrix[y - 1][x])
            cost_matrix[y][x] = abs(elem1 - elem2) + penalty

    return cost_matrix


def get_optimal_path(
        cost_matrix: Matrix
) -> Tuple[Sequence[Tuple[int, int]], Sequence[int]]:
    optimal_path_coords, optimal_path_costs = [], []
    y, x = len(cost_matrix) - 1, len(cost_matrix[0]) - 1

    while True:
        optimal_path_coords.append((x, y))
        optimal_path_costs.append(cost_matrix[y][x])
        if x == 0 and y == 0:
            break
        elif x == 0:
            y -= 1
        elif y == 0:
            x -= 1
        else:
            horizontal_cost = cost_matrix[y][x - 1]
            diagonal_cost = cost_matrix[y - 1][x - 1]
            vertical_cost = cost_matrix[y - 1][x]
            if horizontal_cost < diagonal_cost:
                if horizontal_cost < vertical_cost:
                    x -= 1
                else:
                    y -= 1
            else:
                y -= 1
                if diagonal_cost <= vertical_cost:
                    x -= 1

    return optimal_path_coords[::-1], optimal_path_costs[::-1]


def run(
    seq1: Sequence[int], seq2: Sequence[int]
) -> Tuple[Sequence[Tuple[int, int]], Sequence[int], Matrix]:
    cost_matrix = get_cost_matrix(seq1, seq2)
    optimal_path_coords, optimal_path_costs = get_optimal_path(cost_matrix)
    return optimal_path_coords, optimal_path_costs, cost_matrix