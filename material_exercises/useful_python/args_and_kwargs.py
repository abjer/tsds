

''' Arguments and keyword arguments

Whenever you need to pass a variable number of
arguments to a function you can use arguments
and keyword arguments. Unnamed arguments are
supplied by giving a function an argument
followed by a *. Optional named arguments are
given by passing an argument preceeded by **.
'''


def check_all_int(*a):
    for var in a:
        if not isinstance(var, int):
            return False
    return True


def set_vals_in_dict(dictionary, **kw):
    for k,v in kw.items():
        dictionary[k] = v
    return dictionary



if __name__ == '__main__':
    v = 'not an int'
    w = -1
    x = 1
    y = 2.5
    z = 3

    print('All inputs are integers: {}'.format( check_all_int(v,w,x,y,z) ) )
    print('w,x,z are integers: {}'.format( check_all_int(w,x,z) ) )


    d = {'a':1, 'b':2, 'c':3, 'd':4}
    print('Setting a=-1 and c=2: {}'.format( set_vals_in_dict(d, a=-1, c=2, f='hello') ) )


    # These also work in reverse
    maybe_int = ('not a number', 1, 3, -2, 0.4)

    print('Checking if content in maybe_int is integers {}'.format( check_all_int(*maybe_int) ) )

