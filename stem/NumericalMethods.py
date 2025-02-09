from copy import deepcopy

from NumericalMethods import GaussSeidel

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    This funciton implements th Secant method to find the root of an equation.  You should write your equation in a form
    fcn = 0 such that when the correct value of x is selected, the fcn actually equals zero (or very close to it).
    :param fcn: the function for which we want to find the root
    :param x0: x value in neighborhood of root (or guess 1)
    :param x1: another x value in neighborhood of root (or guess x0+1)
    :param maxiter: exit if the number of iterations (new x values) equals this number
    :param xtol:  exit if the |xnewest - xprevious| < xtol
    :return: tuple with: (the final estimate of the root (most recent value of x), number of iterations)
    """
    pass

def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    Aaug = GE.MakeDiagDom(Aaug)
    pass

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
