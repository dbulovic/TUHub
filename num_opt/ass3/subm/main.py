import numpy as np
from scipy.optimize import approx_fprime
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import json


class NN(object):
    def __init__(self, num_input: int, num_hidden: int, num_output: int, gradient_method: str, dtype=np.float32):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output
        self.dtype = dtype
        self.gradient_method = gradient_method

        self.init_params()

    def init_params(self):
        self.theta = {}
        self.theta['W0'] = np.array(0)
        self.theta['W1'] = np.array(0)
        self.theta['b0'] = np.array(0)
        self.theta['b1'] = np.array(0)

    def export_model(self):
        with open(f'model_{self.gradient_method}.json', 'w') as fp:
            json.dump({key: value.tolist() for key, value in self.theta.items()}, fp)


def task1():
    """ Neural Network

        Requirements for the plots:
            - ax[0] Plot showing the training loss for both variants
            - ax[1] Plot showing the training and test accuracy for both variants
    """
    input_size = 4
    output_size = 3
    hidden_size = 16

    w0 = np.random.normal(0, 0.05, (hidden_size, 4))
    b0 = np.random.normal(0, 0.05, hidden_size)
    w1 = np.random.normal(0, 0.05, (3, hidden_size))
    b1 = np.random.normal(0, 0.05, 3)

    # Create the models
    # Model using steepest descent
    net_GD = NN(1, 1, 1, gradient_method='GD')
    net_GD.theta['W0'] = w0
    net_GD.theta['b0'] = b0
    net_GD.theta['W1'] = w1
    net_GD.theta['b1'] = b1

    # Model using Nesterovs method
    net_NAG = NN(1, 1, 1, gradient_method='NAG')
    net_NAG.theta['W0'] = w0
    net_NAG.theta['b0'] = b0
    net_NAG.theta['W1'] = w1
    net_NAG.theta['b1'] = b1

    net_GD.export_model()
    net_NAG.export_model()

    # Configure plot
    fig = plt.figure(figsize=[12,6])
    axs = []
    axs.append(fig.add_subplot(121))
    axs.append(fig.add_subplot(122))

    axs[0].set_title('Loss')
    axs[0].grid()

    axs[1].set_title('Accuracy')
    axs[1].grid()
    return fig

if __name__ == '__main__':

    # load the data set
    with np.load('data_train.npz') as data_set:
        # get the training data
        x_train_g = data_set['x']
        y_train_g = data_set['y']

    with np.load('data_test.npz') as data_set:
        # get the test data
        x_test_g = data_set['x']
        y_test_g = data_set['y']

    print(f'Training set with {x_train_g.shape[0]} data samples.')
    print(f'Test set with {x_test_g.shape[0]} data samples.')

    tasks = [task1]

    pdf = PdfPages('figures.pdf')
    for task in tasks:
        retval = task()
        fig = retval[0] if type(retval) is tuple else retval
        pdf.savefig(fig)
    pdf.close()

    
