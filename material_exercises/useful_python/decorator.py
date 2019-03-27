

''' Decorators:

    Use decorators when you want to wrap an already written
    function in additional code, expecially when you want to
    do this to multiple functions.

    For example: imagine you have data x,y and you want to
    plot these data. You might want to apply a transformation
    to the data before plotting, e.g. take the log or remove
    outliers.

'''

import matplotlib.pyplot as plt
from numpy import exp, log


def plot(x,y):
    ' Plot a scatter plot of x and y. '
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x, y, color = 'blue')

    return ax


# This defines our decorators:
def loglog(func):
    ' Plot with log-log axis'
    def inner(x,y):
        axis =  func(log(x), log(y))
        axis.set_title("Log-log plot")
        return axis
    return inner


def logy(func):
    'Plot with log y axis'
    def inner(x,y):
        axis = func(x, log(y))
        axis.set_title("Log-y plot")
        return axis
    return inner



# Now lets apply our decorators
# to quickly modify the original plot
@loglog
def loglogplot(x,y):
    return plot(x,y)


@logy
def logyplot(x,y):
    return plot(x,y)



def f(x):
    return x


def deco(func):
    def inner(x):
        print('before')
        print(func(x))
        print('after')
    return inner


@deco
def g(x):
    return f(x)



# This runs the script
if __name__ == '__main__':
    x = range(100)
    y = [exp(i) for i in x]

    plot(x,y)
    plt.show()

    loglogplot(x,y)
    plt.show()

    logyplot(x,y)
    plt.show()

    g(100)
