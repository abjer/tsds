''' Context managers are what you see when
    you use the 'with' keyword. They are,
    as the name suggests, intended to use
    for managing the context of some code.

    The most common example is loading a
    file from disk. Since this involves
    opening a file, under the hood python
    gets a file descriptor from the OS.
    Since these are a finite ressource,
    python should let the OS know that
    it is done using the file. In code we
    implement this by typing

        with open('filepath.txt', 'r') as f:
            f.read()

    as opposed to simply

        f = open('filepath.txt', 'r')

    which doesn't close the file after use.

    We can write our own context managers:
'''

import pandas as pd


class Collapsed:
    def __init__(self, df, *groups, **opts):
        self.df = df
        self.funcs = opts.get('funcs', 'mean')
        self.groups = groups

    def __enter__(self):
        collapsed = self.df.groupby(list(self.groups))\
                           .agg(self.funcs)\
                           .reset_index(drop = False)

        return collapsed

    def __exit__(self, type, value, traceback):
        pass




if __name__ == '__main__':

    data = {'group': [1,1,1,2,2,2], 'values': [1,2,3,4,5,6]}
    df = pd.DataFrame(data)

    print('-------------------')
    print(df)

    with Collapsed(df, 'group') as c:
        print('--------------------')
        print(c)

        