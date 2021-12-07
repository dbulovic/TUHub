#!/usr/bin/env python

""" Python code submission file.

IMPORTANT:
- Do not include any additional python packages.
- Do not change the existing interface and return values of the task functions.
- Prior to your submission, check that the pdf showing your plots is generated.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy import optimize
from scipy.optimize import approx_fprime, linprog
from typing import Callable

# Modify the following global variables to be used in your functions
""" Start of your code
"""

alpha = 2
beta = 15

d = 2.5
b = np.random.randn(5)
D = np.random.randn(5, 5)
A = np.random.randn(5, 5)

""" End of your code
"""

def task1():

    """ Characterization of Functions

        Requirements for the plots:
            - ax[0, 0] Contour plot for a)
            - ax[0, 1] Contour plot for b)
            - ax[1, 0] Contour plot for c)
            - ax[1, 1] Contour plot for d)
    """

    fig, ax = plt.subplots(2, 2, figsize=(12,12))
    fig.suptitle('Task 1 - Contour plots of functions', fontsize=16)

    ax[0, 0].set_title('a)')
    ax[0, 0].set_xlabel('$x_1$')
    ax[0, 0].set_ylabel('$x_2$')

    ax[0, 1].set_title('b)')
    ax[0, 1].set_xlabel('$x_1$')
    ax[0, 1].set_ylabel('$x_2$')

    ax[1, 0].set_title('c)')
    ax[1, 0].set_xlabel('$x_1$')
    ax[1, 0].set_ylabel('$x_2$')

    ax[1, 1].set_title('d)')
    ax[1, 1].set_xlabel('$x_1$')
    ax[1, 1].set_ylabel('$x_2$')

    """ Start of your code
    """

    x1, x2 = np.meshgrid(np.linspace(-5, 5), np.linspace(-10, 10))
    ax[0, 0].contour(x1, x2, (-x1 + 3*x2 - d)**2)
    ax[0, 0].plot(-5, (1/3)*(-5) + 5/6, 'bx')
    ax[0, 0].plot(-4, (1/3)*(-4) + 5/6, 'bx')
    ax[0, 0].plot(-3, (1/3)*(-3) + 5/6, 'bx')
    ax[0, 0].plot(-2, (1/3)*(-2) + 5/6, 'bx')
    ax[0, 0].plot(-1, (1/3)*(-1) + 5/6, 'bx')
    ax[0, 0].plot(0, 5/6, 'bx')
    ax[0, 0].plot(1, (1/3)*(1) + 5/6, 'bx')
    ax[0, 0].plot(2, (1/3)*(2) + 5/6, 'bx')
    ax[0, 0].plot(3, (1/3)*(3) + 5/6, 'bx')
    ax[0, 0].plot(4, (1/3)*(4) + 5/6, 'bx')
    ax[0, 0].plot(5, (1/3)*(5) + 5/6, 'bx')

    x1, x2 = np.meshgrid(np.linspace(-2, 4), np.linspace(-3, 3))
    ax[0, 1].contour(x1, x2, (x1 - 2)**2 + x1*(x2**2) - 2, 2)
    ax[0, 1].plot(2, 0, 'bx')
    ax[0, 1].plot(0, 2, 'bx')
    ax[0, 1].plot(0, -2, 'bx')

    x1, x2 = np.meshgrid(np.linspace(-2, 1), np.linspace(-2, 2))
    ax[1, 0].contour(x1, x2, (x1**3)+ 2*(x1**2) + x1*((x2)**2) + (x2**2))
    ax[1, 0].plot(-1, 1, 'bx')
    ax[1, 0].plot(-1, -1, 'bx')
    ax[1, 0].plot(0, 0, 'bx')
    ax[1, 0].plot(-4/3, 0, 'bx')

    x1, x2 = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
    ax[1, 1].contour(x1, x2, alpha*x1**2 - 2*x1 + beta*x2**2)
    ax[1, 1].plot(1/2, 0, 'bx')

    """ End of your code
    """
    return fig

# Modify the function bodies below to be used for function value and gradient computation
def approx_grad_task1(func: Callable[[np.ndarray], float], x: np.ndarray) -> np.ndarray:
    
    """ Numerical Gradient Computation
        @param x Vector of size (2,)
        This function shall compute the gradient approximation for a given point 'x' and a function 'func'
        using the given central differences formulation for 2D functions. (Task1 functions)
        @return The gradient approximation
    """
    assert(len(x) == 2)
    epsilon = 0.0001
    return np.array([1/(2*epsilon)* (func([x[0] + epsilon, x[1]]) - func([x[0] - epsilon, x[1]])), 
                     1/(2*epsilon)* (func([x[0], x[1] + epsilon]) - func([x[0], x[1] - epsilon]))])

def approx_grad_task2(func: Callable[[np.ndarray], float], x: np.ndarray) -> np.ndarray:
    
    """ Numerical Gradient Computation
        @param x Vector of size (n,)
        This function shall compute the gradient approximation for a given point 'x' and a function 'func'
        using scipy.optimize.approx_fprime(). (Task2 functions)
        @return The gradient approximation
    """
    return approx_fprime(x.squeeze(), func, 1e-4)

def func_1a(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 1a) at a given point x
        @param x Vector of size (2,)
    """
    return (-x[0] + 3*x[1] - d)**2

def grad_1a(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 1a) at a given point x
        @param x Vector of size (2,)
    """
    return np.array([-2*(-x[0] + 3*x[1] - d), 6*(-x[0] + 3*x[1] - d)])

def func_1b(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 1b) at a given point x
        @param x Vector of size (2,)
    """
    return (x[0] - 2)**2 + x[0]*x[1]**2 - 2

def grad_1b(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 1b) at a given point x
        @param x Vector of size (2,)
    """
    return np.array([2*x[0] - 4 + x[1]**2, 2*x[0]*x[1]])

def func_1c(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 1c) at a given point x
        @param x Vector of size (2,)
    """
    return x[0]**3 + 2*x[0]**2 + x[0]*x[1]**2 + x[1]**2

def grad_1c(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 1c) at a given point x
        @param x Vector of size (2,)
    """
    return np.array([3*x[0]**2 + 4*x[0] + x[1]**2, 2*x[0]*x[1] + 2*x[1]])

def func_1d(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 1d) at a given point x
        @param x Vector of size (2,)
    """
    return alpha*x[0]**2 - 2*x[0] + beta*x[1]**2

def grad_1d(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 1d) at a given point x
        @param x Vector of size (2,)
    """
    return np.array([2*alpha*x[0] - 2, 2*beta*x[1]])

def func_2a(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 2a) at a given point x
        @param x Vector of size (n,)
    """
    return 1/4*(np.linalg.norm(x-b)**4)

def grad_2a(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 2a) at a given point x
        @param x Vector of size (n,)
    """
    return np.dot(np.linalg.norm(x - b)**2, (x - b))

def func_2b(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 2b) at a given point x
        @param x Vector of size (n,)
    """
    def g(z):
        return 1/2*z**2 + z

    return np.sum(np.array([g((A@x)[i]) for i in range(5)]))

def grad_2b(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 2b) at a given point x
        @param x Vector of size (n,)
    """
    return(A.T@(A@x + 1))

def func_2c(x: np.ndarray) -> float:
    """ Computes and returns the function value for function 2c) at a given point x
        @param x Vector of size (n,)
    """
    return (x/b).T@D@(x / b)

def grad_2c(x: np.ndarray) -> np.ndarray:
    """ Computes and returns the analytical gradient result for function 2c) at a given point x
        @param x Vector of size (n,)
    """
    return (D@(x/b)/b + D.T@(x/b)/b)

def task3():

    """ Numerical Gradient Verification
        ax[0] to ax[3] Bar plot comparison, analytical vs numerical gradient for Task 1
        ax[4] to ax[6] Bar plot comparison, analytical vs numerical gradient for Task 2

    """
    n = 5
    fig = plt.figure(figsize=(15,10), constrained_layout=True)
    fig.suptitle('Task 3 - Barplots numerical vs analytical', fontsize=16)
    ax = [None, None, None, None, None, None, None]
    keys = ['a)', 'b)', 'c)', 'd)']
    gs = fig.add_gridspec(7, 12)

    n = 2
    for i in range(4):
        ax[i] = fig.add_subplot(gs[1:4, 3*i:(3*i+3)])
        ax[i].set_title('1 '+keys[i])
        ax[i].set_xticks(np.arange(n))
        ax[i].set_xticklabels((r'$\frac{\partial}{\partial x_1}$', r'$\frac{\partial}{\partial x_2}$'), fontsize=16)

    n = 5
    for k, i in enumerate(range(4, 7)):
        ax[i] = fig.add_subplot(gs[4:, 4*k:(4*k+4)])
        ax[i].set_title('2 '+ keys[k])
        ax[i].set_xticks(np.arange(n))
        ax[i].set_xticklabels((r'$\frac{\partial}{\partial x_1}$', r'$\frac{\partial}{\partial x_2}$', r'$\frac{\partial}{\partial x_3}$', r'$\frac{\partial}{\partial x_4}$', r'$\frac{\partial}{\partial x_5}$'), fontsize=16)

    """ Start of your code
    """

    # Example for plot usage
    bw = 0.3

    x0 = np.random.randn(2)

    app_1a = approx_grad_task1(func_1a, x0)
    gr_1a = grad_1a(x0)
    ax[0].bar([0-bw/2,1-bw/2], [app_1a[i] for i in range(2)], bw)
    ax[0].bar([0+bw/2,1+bw/2], [gr_1a[i] for i in range(2)], bw)

    app_1b = approx_grad_task1(func_1b, x0)
    gr_1b = grad_1b(x0)
    ax[1].bar([0-bw/2,1-bw/2], [app_1b[i] for i in range(2)], bw)
    ax[1].bar([0+bw/2,1+bw/2], [gr_1b[i] for i in range(2)], bw)

    app_1c = approx_grad_task1(func_1c, x0)
    gr_1c = grad_1c(x0)
    ax[2].bar([0-bw/2,1-bw/2], [app_1c[i] for i in range(2)], bw)
    ax[2].bar([0+bw/2,1+bw/2], [gr_1c[i] for i in range(2)], bw)

    app_1d = approx_grad_task1(func_1d, x0)
    gr_1d = grad_1d(x0)
    ax[3].bar([0-bw/2,1-bw/2], [app_1d[i] for i in range(2)], bw)
    ax[3].bar([0+bw/2,1+bw/2], [gr_1d[i] for i in range(2)], bw)

    x0 = np.random.randn(5)

    app_2a = approx_grad_task2(func_2a, x0)
    gr_2a = grad_2a(x0)
    ax[4].bar([i - bw/2 for i in range(5)], [app_2a[i] for i in range(5)], bw)
    ax[4].bar([i + bw/2 for i in range(5)], [gr_2a[i] for i in range(5)], bw)

    app_2b = approx_grad_task2(func_2b, x0) 
    gr_2b = grad_2b(x0)
    ax[5].bar([i - bw/2 for i in range(5)], [app_2b[i] for i in range(5)], bw)
    ax[5].bar([i + bw/2 for i in range(5)], [gr_2b[i] for i in range(5)], bw)

    app_2c = approx_grad_task2(func_2c, x0)
    gr_2c = grad_2c(x0)
    ax[6].bar([i - bw/2 for i in range(5)], [app_2c[i] for i in range(5)], bw)
    ax[6].bar([i + bw/2 for i in range(5)], [gr_2c[i] for i in range(5)], bw)
    

    """ End of your code
    """
    return fig


def task4():

    """ Scheduling Optimization Problem
        @return The scheduling plan M
    """

    """ Start of your code
    """
    A = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],

        [-1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1],

        [1 for i in range(8)] + [0 for i in range(8)],

        [0 for i in range(8)] + [1 for i in range(8)],

        [-1] + [0 for i in range(15)],
        [0, -1] + [0 for i in range(14)],
        [0, 0, -1] + [0 for i in range(13)],
    ])

    b = np.array([
        1200, 1500, 1400, 400, 1000, 800, 760, 1300,
        -1200, -1500, -1400, -400, -1000, -800, -760, -1300,
        4500, 4500,
        -0.4*1200, -0.4*1500, -0.4*1400
    ])

    c = np.array([0.11, 0.13, 0.09, 0.12, 0.15, 0.14, 0.11, 0.12,
                  0.10, 0.13, 0.08, 0.13, 0.14, 0.14, 0.09, 0.13])
    result = optimize.linprog(c, A_ub=A, b_ub=b)
    
    res_int = [0 for i in range(16)]
    for i in range(16):
        res_int[i] = round(result.x[i])

    M = np.array([[i for i in res_int[:8]], [i for i in res_int[8:]]])
    M = (M.T).tolist()
    for i in range(8):
        for j in range(2):
            print(M[i][j], end=' ')
        print("")

    sum = 0
    for i in range(16):
        sum += res_int[i]*c[i]
    
    print(sum, result.fun)

    """ End of your code
    """
    return M

if __name__ == '__main__':
    tasks = [task1, task3]

    pdf = PdfPages('figures.pdf')
    for task in tasks:
        retval = task()
        pdf.savefig(retval)
    pdf.close()

    task4()