from copy import deepcopy

from NumericalMethods import GaussSeidel


def main():
    print("run Gauss-Seidel solver:")
    Aaug1 = [
        [3, 1, -1, 2],
        [1, 4, 1, 12],
        [2, 1, 2, 10]
    ]

    Aaug2 = [
        [1, -10, 2, 4, 2],
        [3, 1, 4, 12, 12],
        [9, 2, 3, 4, 21],
        [-1, 2, 7, 3, 37]
    ]

    x0_3 = [0, 0, 0]
    x0_4 = [0, 0, 0, 0]
    Niter = 15

    print("calling GaussSeidel for 1st system:")
    solution1 = GaussSeidel(Aaug1, x0_3, Niter)

    print("calling GaussSeidel for 2nd system:")
    solution2 = GaussSeidel(Aaug2, x0_4, Niter)

    print("\nSolution for 1st system 3x3:")
    for i, val in enumerate(solution1):
        print(f"x{i + 1}={val:.6f}")

    print("\nSolution for 2nd system 4x4:")
    for i, val in enumerate(solution2):
        print(f"x{i + 1}={val:.6f}")


if __name__ == "__main__":
    main()
