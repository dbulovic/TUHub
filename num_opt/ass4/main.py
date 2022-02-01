import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.optimize
from matplotlib.backends.backend_pdf import PdfPages


def power_iteration(M: np.array, eps:float=1e-8) -> float:

    assert len(M.shape) == 2, 'M must be matrix with 2 dimensions'
    assert M.shape[0] == M.shape[1], 'M must be a square matrix'

    d = M.shape[1]

    v = np.ones(d) / np.sqrt(d)
    ev = v @ M @ v

    while True:
        Mv = M @ v
        v_new = Mv / (np.linalg.norm(Mv))

        ev_new = v_new @ M @ v_new
        if np.abs(ev - ev_new) < eps:
            break

        v = v_new
        ev = ev_new

    # Retrun the largest eigenvalue
    return ev_new


def task1(signal):
    """ Signal Denoising

        Requirements for the plots:
            -ax[0,0] - Results for low noise and K=15
            -ax[0,1] - Results for high noise and K=15
            -ax[1,0] - Results for low noise and K=100
            -ax[1,1] - Results for low noise and K=5

    """

    fig, ax = plt.subplots(2, 2, figsize=(16,8))
    fig.suptitle('Task 1 - Signal denoising task', fontsize=16)

    ax[0,0].set_title('a)')

    ax[0,1].set_title('b)')

    ax[1,0].set_title('c)')

    ax[1,1].set_title('d)')

    """ Start of your code
    """

    n = len(signal)

    def get_A(d):
        Atmp = []
        for i in range(n):
            tmpr = []
            for j in range(d):
                if j + 1 == 1:
                    alph = 1/((n)**(1/2))
                else: 
                    alph = (2/n)**(1/2)
                tmpr.append(alph*np.cos(np.pi/n)*(j)*(i + 1/2))
            Atmp.append(tmpr)
        A = np.array(Atmp)
        return A

    def get_b(sigma):
        ns_signal = [0 for i in range(len(signal))]
        for i in range(len(signal)):
            ns_signal[i] = signal[i] + np.random.normal(0, sigma)

        b = np.array(ns_signal)
        return b

    # def frst_f(xt:np.ndarray):
    #     return 1/2*((np.linalg.norm(A@xt - b))**2)

    def frank_wolfe(sigma, d, k):
        xtmp = [1/d for i in range(d)]
        x = np.array(xtmp)

        A = get_A(d)
        b = get_b(sigma)

        for ki in range(k):
            deltaf1 = A.T@(A@x - b)
            
            i = np.argmin(deltaf1)

            ytmp = []
            for j in range(d):
                if i == j: ytmp.append(1)
                else: ytmp.append(0)

            y = np.array(ytmp)

            t = 2/(ki+1)

            x = (1-t)*x+t*y
        return x, A, b

    xa, A, b = frank_wolfe(0.01, 15, 1000)
    res1 = A@xa
    ax[0,0].plot(signal)
    ax[0,0].plot(b)
    ax[0,0].plot(res1)

    xb, A, b = frank_wolfe(0.03, 15, 1000)
    res2 = A@xb
    ax[0,1].plot(signal)
    ax[0,1].plot(b)
    ax[0,1].plot(res2)

    xc, A, b = frank_wolfe(0.01, 100, 10000)
    res3 = A@xc
    ax[1,0].plot(signal)
    ax[1,0].plot(b)
    ax[1,0].plot(res3)

    xd, A, b = frank_wolfe(0.01, 5, 1000)
    res4 = A@xd
    ax[1,1].plot(signal)
    ax[1,1].plot(b)
    ax[1,1].plot(res4)

    """ End of your code
    """

    return fig


def task2(img):

    """ Image Representation

        Requirements for the plots:
            - ax[0] The ground truth image
            - ax[1] Reconstructed image using proj. GD
            - ax[2] Reconstructed image using Frank-Wolfe algorithm
            - ax[3] Semilogarithmic plot comparing the energies over
                    iterations for both methods
    """

    fig = plt.figure(figsize=(11,9), constrained_layout=True)
    fig.suptitle('Task 2 - Image Representation', fontsize=16)
    ax = [None, None, None, None]
    g = fig.add_gridspec(9, 9)
    ax[0] = fig.add_subplot(g[1:4:, 0:3])
    ax[1] = fig.add_subplot(g[1:4:, 3:6])
    ax[2] = fig.add_subplot(g[1:4:, 6:])
    ax[3] = fig.add_subplot(g[4:, :])

    for ax_ in ax[:-1]:
        ax_.set_aspect('equal')
        ax_.get_xaxis().set_visible(False)
        ax_.get_yaxis().set_visible(False)
    
    ax[0].set_title('GT')
    ax[1].set_title('Proj. GD')
    ax[2].set_title('Frank-Wolfe')
    
    """ Start of your code
    """

    """ End of your code
    """

    return fig

    
if __name__ == "__main__":
    args = []
    with np.load('data.npz') as data:
        args.append(data['sig'])
        args.append(data['yoshi'])
    
    pdf = PdfPages('figures.pdf')

    for task, arg in zip([task1, task2], args):
        retval = task(arg)
        fig = retval[0] if type(retval) is tuple else retval
        pdf.savefig(fig)
    pdf.close()