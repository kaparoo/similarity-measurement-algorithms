# -*- coding: utf-8 -*-

from absl import app
from absl import flags

import dynamic_time_wraping as dtw
import utils

_ENABLE_ALGORITHMS = ["dtw"]

FLAGS = flags.FLAGS
flags.DEFINE_enum("algorithm", "dtw", _ENABLE_ALGORITHMS, "Algorithms")
flags.DEFINE_list("seq1", "1, 7, 3, 4, 1, 10, 5, 4, 7, 4",
                  "Integer sequence for x-axis")
flags.DEFINE_list("seq2", "1, 4, 5, 10, 9, 3, 2, 6, 8, 4",
                  "Integer Sequence for y-axis")


def main(_):
    seq1 = [int(e) for e in FLAGS.seq1]
    seq2 = [int(e) for e in FLAGS.seq2]

    algorithm = FLAGS.algorithm
    if algorithm == "dtw":
        optimal_pairs, optimal_costs, cost_matrix = dtw.run(seq1, seq2)
        utils.display_matrix(cost_matrix)
        print("seq1 (x-axis):", seq1)  # [1, 7, 3, 4, 1, 10, 5, 4, 7, 4]
        print("seq2 (y-axis):", seq2)  # [1, 4, 5, 10, 9, 3, 2, 6, 8, 4]
        # [(0, 0), (1, 1), (2, 1), (3, 1), (4, 2), (5, 3),
        #  (5, 4), (6, 5), (7, 6), (8, 7), (8, 8), (9, 9)]
        print("optimal_pairs [(x, y)]:", optimal_pairs)
        # [0, 3, 4, 4, 8, 8, 9, 11, 13, 14, 15, 15]
        print("optimal_costs:", optimal_costs)


if __name__ == "__main__":
    app.run(main)