#!/usr/bin/env python

""" Python code submission file.

IMPORTANT:
- Do not include any additional python packages.
- Do not change the existing interface and return values of the task functions.
- Prior to your submission, check that the pdf showing your plots is generated.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.lib.function_base import meshgrid
from scipy.linalg import inv
from matplotlib.backends.backend_pdf import PdfPages
from typing import Callable


def task1():

    """ Lagrange Multiplier Problem

        Requirements for the plots:
            - ax[0] Contour plot for a)
            - ax[1] Contour plot for b)
            - ax[2] Contour plot for c)
    """

    fig, ax = plt.subplots(1, 3, figsize=(18,6))
    fig.suptitle('Task 1 - Contour plots + Constraints', fontsize=16)

    ax[0].set_title('a)')
    ax[0].set_xlabel('$x_1$')
    ax[0].set_ylabel('$x_2$')
    ax[0].set_aspect('equal')

    ax[1].set_title('b)')
    ax[1].set_xlabel('$x_1$')
    ax[1].set_ylabel('$x_2$')
    ax[1].set_aspect('equal')

    ax[2].set_title('c)')
    ax[2].set_xlabel('$x_1$')
    ax[2].set_ylabel('$x_2$')
    ax[2].set_aspect('equal')


    """ Start of your code
    """
    # Plot example (remove in submission)
    x1, x2 = np.meshgrid(np.linspace(-7, 7), np.linspace(-7, 7))
    ax[0].contourf(x1, x2, x2 - x1, 100, cmap='gist_rainbow')
    ax[0].plot(np.linspace(-28, 28), np.linspace(-7, 7))
    def f1(x): return 1/10*x**2-3
    ax[0].plot(x1, f1(x1), "go", markersize=2)
    ax[0].scatter(5, -1/2, color="black", marker="o")
    ax[0].scatter(5/4 + (505)**(1/2)/4, 5/16 + (505)**(1/2)/16, color="red", marker="o")
    ax[0].scatter(5/4 - (505)**(1/2)/4, 5/16 - (505)**(1/2)/16, color="red", marker="o")
    ax[0].set_xlim([-7, 7]) 
    ax[0].set_ylim([-7, 7])

    ax[1].contourf(x1, x2, x1**2 + x2**2, 100, cmap='gist_rainbow')
    ax[1].plot(np.linspace(-7, 7), np.linspace(10, -4))
    ax[1].plot(np.linspace(-7, 7), np.linspace(2, 2))
    ax[1].scatter(1, 2, color="black")
    ax[1].set_xlim([-7, 7]) 
    ax[1].set_ylim([-7, 7])

    x1, x2 = np.meshgrid(np.linspace(-3, 3), np.linspace(-3, 3))
    ax[2].contourf(x1, x2, (x1 - 1)**2 + x1 * x2**2  - 2, 100, cmap='gist_rainbow')
    ax[2].scatter(1, 0, color="blue")
    ax[2].scatter(0, 2**(1/2), color="red")
    ax[2].scatter(0, -(2**(1/2)), color="red")
    ax[2].scatter(1/3*(1 - 7**(1/2)), (-1/3)*((2*(14+7**(1/2)))**(1/2)), color="red")
    ax[2].scatter(1/3*(1 - 7**(1/2)), (1/3)*((2*(14+7**(1/2)))**(1/2)), color="red")
    ax[2].scatter(1/3*(1 + 7**(1/2)), (-1/3)*((2*(14-7**(1/2)))**(1/2)), color="red")
    ax[2].scatter(-2, 0, color="red")
    ax[2].scatter(2, 0, color="red")
    circle = plt.Circle((0,0), 2, fill=False)
    ax[2].add_patch(circle)
    ax[2].set_xlim([-3, 3])
    ax[2].set_ylim([-3, 3])

    """ End of your code
    """
    return fig


def task2():

    """ Lagrange Augmentation
        ax Filled contour plot including the constraints and the iterates of x_k

    """
    fig, ax = plt.subplots(1, 1, figsize=(8,8))
    fig.suptitle('Task 2 - Contour plots + Constraints + Iterations over k', fontsize=16)
    """ Start of your code
    """
    size = 15
    x1, x2 = np.meshgrid(np.linspace(-size, size), np.linspace(-size, size))
    ax.contourf(x1, x2, (x1 - 1)**2 - x1*x2, 100, cmap='gist_rainbow')
    ax.plot(np.linspace(-20, 20), np.linspace(24, -16))
    ax.scatter(3/2, 5/2, color="black", marker="o")
    ax.set_xlim([-size, size]) 
    ax.set_ylim([-size, size])

    lambda_k = -1
    alpha = 0.7
    k = 20

    for i in range(k):
        x1 = (6*alpha + lambda_k)/(4*alpha - 1)
        x2 = (10*alpha +3*lambda_k + 2)/(4*alpha - 1)
        ax.scatter(x1, x2, color="white", marker="x")
        lambda_k = alpha*(-x1 - x2 -4) + lambda_k



    """ End of your code
    """
    return fig


def task3():

    """ Least Squares Fitting
        ax 3D scatter plot and wireframe of the computed solution
    """
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    fig.suptitle('Task 3 - Data points vs. LS solution', fontsize=16)

    with np.load('data.npz') as fc:
        x = fc['data'][:,0]
        y = fc['data'][:,1]
        z = fc['data'][:,2]
    
    N = len(x)
    A = None
    x_solution = None
    """ Start of your code
    """

    ax.scatter(x, y, z)

    def f(x, y):
        return [1, y, y**2, y**3, \
                x, x*y, x*(y**2), x*(y**3), \
                (x**2), (x**2)*y, (x**2)*(y**2), (x**2)*(y**3), \
                (x**3), (x**3)*y, (x**3)*(y**2), (x**3)*(y**3)]
    
    tmp_arr = []
    for i in range(N):
        tmp_arr.append(f(x[i], y[i]))
    
    A = np.array(tmp_arr)

    x_solution = inv(A.T@A)@A.T@z
    

    x1 = np.linspace(-4, 4, 50)
    y1 = np.linspace(-4, 4, 50)
    x, y = np.meshgrid(x1,y1)

    z = 1*x_solution[0] + y*x_solution[1] + y**2*x_solution[2] + y**3*x_solution[3] + \
                x*x_solution[4] + x*y*x_solution[5] + x*(y**2)*x_solution[6] + x*(y**3)*x_solution[7] + \
                (x**2)*x_solution[8] + (x**2)*y*x_solution[9] + (x**2)*(y**2)*x_solution[10] + (x**2)*(y**3)*x_solution[11] + \
                (x**3)*x_solution[12] + (x**3)*y*x_solution[13] + (x**3)*(y**2)*x_solution[14] + (x**3)*(y**3)*x_solution[15]

    ax.plot_wireframe(x, y, z)

    print(x_solution)

    """ End of your code
    """
    return fig, A, x_solution


if __name__ == '__main__':
    tasks = [task1, task2, task3]

    pdf = PdfPages('figures.pdf')
    for task in tasks:
        retval = task()
        fig = retval[0] if type(retval) is tuple else retval
        pdf.savefig(fig)
    pdf.close()
