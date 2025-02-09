#region imports
import math
import copy
import Gauss_Elim as GE  # this is the module from lecture 2 that has usefule matrix manipulation functions
from math import sqrt, pi, exp, cos
#endregion

#region function definitions
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    Step 1:  unpack args into mu and stDev
    Step 2:  compute lhl and rhl for Simpson
    Step 3:  package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4:  call Simpson with GNPDF and args1
    Step 5:  return probability
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    mu, sig = args
    if GT :
        return 1-Simpson(PDF,(mu, sig, mu - 5 * sig, c))
    else:
        return Simpson(PDF, (mu, sig, mu - 5 * sig, c))


def GPDF(args):
    """
    Here is where I will define the Gaussian probability density function.
    This requires knowing the population mean and standard deviation.
    To compute the GPDF at any value of x, I just need to compute as stated
    in the homework assignment.
    Step 1:  unpack the args tuple into variables called: x, mu, stDev
    Step 2:  compute GPDF value at x
    Step 3:  return value
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    # Step 1: unpack args
    x, mu, sig = args
    # step 2: compute GPDF at x
    fx = (1 / (sig * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sig) ** 2)
    # step 3: return value
    return fx

def Simpson(fn, args, N=100):
    """
    This executes the Simpson 1/3 rule for numerical integration (see page 832, Table 19.4).
    As I recall:
    1. divide the range from x=lhl to x=rhl into an even number of parts. Perhaps 20?
    2. compute fx at each x value between lhl and rhl
    3. sum the even and odd values of fx as prescribed
    4. return the area beneath the function fx
    :param fx: some function of x to integrate
    :param args: a tuple containing (mean, stDev, lhl, rhl)
    :return: the area beneath the function between lhl and rhl
    """
    #unpack args
    mu, sig, a, b = args
    #step size
    h=(b-a)/N
    #x value
    x=[a+ i*h for i in range(N+1)]
    #calculate value
    fx=[fn((xi, mu,sig)) for xi in x]
    #apply simpson formula
    area= fx[0] + fx[-1] + 4*sum(fx[1:N:2])+2*sum(fx[2:N-1:2])
    area= (h/3) * area

    return area

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
    for i in range(maxiter):
        f0, f1 = fcn(x0), fcn(x1)
        if abs(f1-f0) < 1e-12:
            break
        #secant update
        x_new= x1-f1*(x1-x0)/(f1-f0)
        if abs(x_new-x1)<xtol: #stop if close enough
            return x_new, i+1 #return a tuple
        x0, x1=x1, x_new #update guessees
    return x1, maxiter

def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    print("GaussSeidel function running:")
    Aaug = GE.MakeDiagDom(Aaug)
    print("Aaug after MakeDiagDom, Aaug")
    N=len(Aaug)
    for _ in range(Niter):
        for i in range(N):
            sum_=sum(Aaug[i][j] *x[j] for j in range (N) if j !=i)
            x[i]=(Aaug[i][-1] - sum_)/ Aaug [i] [i] #update variable
        print(f"Iteration {_+1}: {x}")
    return x

def main():
    '''
    This is a function I created for testing the numerical methods locally.
    :return: None
    '''
    #region testing GPDF
    fx = GPDF((0,0,1))
    print("{:0.5f}".format(fx))  # Does this match the expected value?
    #edregion

    #region testing Simpson
    p=Simpson(GPDF,(0,1,-5,0)) # should return 0.5
    print("p={:0.5f}".format(p))  # Does this match the expected value?
    #endregion

    #region testing Probability
    p1 = Probability(GPDF, (0,1),0,True)
    print("p1={:0.5f}".format(p1))  # Does this match the expected value?
    #endregion
    pass

#endregion

#region function calls
if __name__ == '__main__':
    main()
#endregion