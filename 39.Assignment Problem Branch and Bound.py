import numpy as np
from scipy.optimize import linear_sum_assignment

def assignment_branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    total_cost = 0

    for _ in range(n):
        min_val = np.min(cost_matrix, axis=1)
        cost_matrix -= min_val[:, np.newaxis]
        min_val = np.min(cost_matrix, axis=0)
        cost_matrix -= min_val

        while True:
            row_idx, col_idx = linear_sum_assignment(cost_matrix)
            total_cost += cost_matrix[row_idx, col_idx].sum()

            if len(row_idx) == n:
                return list(zip(row_idx, col_idx)), total_cost

            min_val = np.min(cost_matrix)
            cost_matrix -= min_val
            cost_matrix[row_idx, col_idx] = np.inf

# Example usage:
if __name__ == "__main__":
    cost_matrix = np.array([[5, 2, 1, 7],
                            [8, 3, 2, 9],
                            [7, 8, 5, 6],
                            [9, 7, 3, 8]])
    assignment, total_cost = assignment_branch_and_bound(cost_matrix)
    print("Assignments:", assignment)
    print("Total cost:", total_cost)
