import numpy as np

def pivot_reorder(matrix:np.ndarray, pivot)->None:
    max_pivot_row = pivot
    maxi = abs(matrix[pivot][pivot])

    for i in range(pivot + 1, len(matrix)):
        if abs(matrix[i][pivot]) > maxi:
            maxi = abs(matrix[i][pivot])
            max_pivot_row = i

    matrix[[pivot, max_pivot_row]] = matrix[[max_pivot_row, pivot]]
    

def find_multiplier(matrix:np.ndarray,pivot:int,zeroing_row:int)->float:
    return matrix[zeroing_row][pivot]/matrix[pivot][pivot]

def normalize_row(matrix:np.ndarray,pivot_row:int,zeroing_row:int,multiplier:float):
    matrix[zeroing_row]-=multiplier*matrix[pivot_row]
    
def renormalize_row(matrix:np.ndarray,row:int)->None:
    matrix[row]/=matrix[row][row]
    
    
def gaussian_jordan_elimination(augmented_matrix:np.ndarray)->None:
    row,col=augmented_matrix.shape
    print(f"row: {row}" )
    print(f"col: {col}" )
    for pivot in range(row):
        pivot_reorder(augmented_matrix,pivot)
        renormalize_row(augmented_matrix,pivot)
        for row_ in range(row):
            if row_==pivot:
                continue
            mul=augmented_matrix[row_][pivot]
            augmented_matrix[row_]-=mul*augmented_matrix[pivot]
            
def back_substitution(matrix:np.ndarray)->list:
    list_=(matrix[:,-1]).tolist()
    return list_


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

    gaussian_jordan_elimination(augmented_matrix)

    print("\nMatrix after Gaussian Elimination:")
    print(augmented_matrix)

    solution = back_substitution(augmented_matrix)

    print("\nSolution:")
    for i, x in enumerate(solution):
        print(f"x{i + 1} = {x}")


if __name__ == "__main__":
    main()