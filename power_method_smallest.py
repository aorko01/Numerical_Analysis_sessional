import numpy as np

def normalize(vector: np.ndarray) -> float:
    maxi = np.max(np.abs(vector))
    vector /= maxi
    return maxi


def power_method(A: np.ndarray, x: np.ndarray, threshold: float):
    x = x.astype(float)

    y = A @ x
    eigen_old = normalize(y)
    x = y

    while True:
        y = A @ x
        eigen_new = normalize(y)
        x = y

        if abs((eigen_new - eigen_old) / eigen_new) <= threshold:
            return eigen_new, x

        eigen_old = eigen_new


def main():
    n = int(input("Enter the order of the matrix: "))

    print(f"Enter the {n}x{n} matrix:")
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        A[i] = list(map(float, input().split()))

    print(f"Enter the initial vector ({n} elements):")
    x = np.array(list(map(float, input().split())), dtype=float)

    threshold = float(input("Enter convergence threshold: "))
    
    A_inv=np.linalg.inv(A)

    eigenvalue, eigenvector = power_method(A_inv, x, threshold)

    print("\nDominant Eigenvalue:")
    print(eigenvalue)

    print("\nDominant Eigenvector:")
    print(eigenvector)


if __name__ == "__main__":
    main()