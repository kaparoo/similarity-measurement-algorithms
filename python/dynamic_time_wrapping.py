# -*- coding: utf-8 -*-

from typing import Callable
from typing import Sequence
from typing import Tuple


def get_cost_matrix(
    seq1: Sequence[int],
    seq2: Sequence[int],
    cost_metric: Callable[[int, int], int] = lambda n1, n2: abs(n1 - n2)
) -> Sequence[Sequence[int]]:
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
            cost_matrix[y][x] = cost_metric(elem1, elem2) + penalty
    return cost_matrix


def get_optimal_path(
    cost_matrix: Sequence[Sequence[int]]
) -> Tuple[Sequence[int], Sequence[Tuple[int, int]]]:
    optimal_costs = []
    optimal_pairs = []
    y, x = len(cost_matrix) - 1, len(cost_matrix[0]) - 1
    while True:
        optimal_pairs.append((x, y))
        optimal_costs.append(cost_matrix[y][x])
        if x == 0 and y == 0:
            break
        elif x == 0:
            y -= 1
        elif y == 0:
            x -= 1
        else:
            cost_leftside = cost_matrix[y][x - 1]
            cost_diagonal = cost_matrix[y - 1][x - 1]
            cost_bottom = cost_matrix[y - 1][x]
            if cost_leftside < cost_diagonal:
                if cost_leftside < cost_bottom:
                    x -= 1
                else:
                    y -= 1
            else:
                y -= 1
                if cost_diagonal <= cost_bottom:
                    x -= 1

    return optimal_pairs[::-1], optimal_costs[::-1]


def run(
    seq1: Sequence[int],
    seq2: Sequence[int],
    cost_metric: Callable[[int, int], int] = lambda x, y: abs(x - y)
) -> Tuple[Sequence[int], Sequence[Tuple[int, int]], Sequence[Sequence[int]]]:
    cost_matrix = get_cost_matrix(seq1, seq2, cost_metric)
    optimal_pairs, optimal_costs = get_optimal_path(cost_matrix)
    return optimal_pairs, optimal_costs, cost_matrix