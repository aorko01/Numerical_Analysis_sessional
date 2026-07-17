import numpy as np


def find_multiplier(matrix: np.ndarray, pivot: int, zeroing_row: int) -> float:
    return matrix[zeroing_row][pivot] / matrix[pivot][pivot]


def normalize_row(
    matrix: np.ndarray, pivot_row: int, zeroing_row: int, multiplier: float
)->None:
    matrix[zeroing_row] -= multiplier * matrix[pivot_row]


def L_U_decomposition(matrix: np.ndarray) -> np.ndarray:
    row, col = matrix.shape
    print(f"row: {row}")
    print(f"col: {col}")
    Lower_matrix = np.zeros((row, col))
    for i in range(len(Lower_matrix)):
        Lower_matrix[i][i] = 1

    for col_ in range(col - 1):
        for row_ in range(col_ + 1, row):
            mul = find_multiplier(matrix, col_, row_)
            Lower_matrix[row_][col_] = mul
            normalize_row(matrix, col_, row_, mul)

    return Lower_matrix


def back_substitution(matrix: np.ndarray) -> list:
    solution = [0.0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        sum_ = sum(matrix[i][j] * solution[j] for j in range(i + 1, len(matrix)))
        solution[i] = (matrix[i][-1] - sum_) / matrix[i][i]

    return solution


def forward_substitution(matrix: np.ndarray) -> list:
    solution = [0.0] * len(matrix)
    for i in range(len(matrix)):
        sum_ = sum(solution[j] * matrix[i][j] for j in range(0, i))
        solution[i] = matrix[i][-1] - sum_

    return solution


def main():
    n = int(input("Enter the number of equations: "))

    print(f"Enter the augmented matrix ({n} rows, {n + 1} values per row):")

    matrix = []

    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))

        if len(row) != n + 1:
            raise ValueError(f"Each row must contain {n + 1} values.")

        matrix.append(row)

    augmented_matrix = np.array(matrix, dtype=float)

    A = augmented_matrix[:, :-1].copy()
    b = augmented_matrix[:, -1].copy()

    L = L_U_decomposition(A)

    U = A

    print("\nL matrix:")
    print(L)

    print("\nU matrix:")
    print(U)

    b = b.reshape(-1, 1)
    L_aug = np.hstack((L, b))

    z = forward_substitution(L_aug)

    print("\nz vector:")
    print(np.array(z))

    z_col = np.array(z).reshape(-1, 1)
    U_aug = np.hstack((U, z_col))

    x = back_substitution(U_aug)

    print("\nSolution x:")
    print(np.array(x))


if __name__ == "__main__":
    main()
