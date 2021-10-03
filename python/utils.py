# -*- coding: utf-8 -*-

import copy
import math
import matplotlib.pyplot as plt

from typing import List, Optional, Sequence, Tuple

Matrix = List[List[int]]


def display_matrix(matrix: Matrix):
    matrix = copy.deepcopy(matrix)[::-1]
    num_digits = int(math.log10(max(map(max, matrix)))) + 1
    for row in matrix:
        for elem in row:
            print(f"[{elem: >{num_digits}d}]", end=" ")
        print()  # New line


def plot_matrix(matrix: Matrix,
                pairs: Optional[Sequence[Tuple[int, int]]] = None):
    plt.pcolor(matrix)
    for x2, row in enumerate(matrix):
        for x1, elem in enumerate(row):
            color = "k"
            if (x1, x2) in pairs:
                color = "w"
            plt.text(x1 + 0.5, x2 + 0.5, elem, color=color)
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    if pairs:
        x1_list = [pair[0] + 0.5 for pair in pairs]
        x2_list = [pair[1] + 0.5 for pair in pairs]
        plt.plot(x1_list, x2_list, 'r')
    plt.show()


def plot_sequences(seq1: Sequence[int],
                   seq2: Sequence[int],
                   pairs: Optional[Sequence[Tuple[int, int]]] = None):
    plt.plot(seq1, 'r')
    plt.plot(seq2, 'b')
    if pairs:
        for coord in pairs:
            x1, x2 = coord
            y1, y2 = seq1[x1], seq2[x2]
            plt.plot([x1, x2], [y1, y2], 'k--')
    plt.show()


def plot_result(seq1: Sequence[int],
                seq2: Sequence[int],
                matrix: Matrix,
                pairs: Optional[Sequence[Tuple[int, int]]] = None):
    pass


if __name__ == "__main__":
    matrix = [[i * j for i in range(1, 9 + 1)] for j in range(1, 9 + 1)]
    pairs = [(i, i) for i in range(0, 9 + 1)]
    display_matrix(matrix)
    plot_matrix(matrix, pairs)