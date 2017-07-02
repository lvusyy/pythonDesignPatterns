import functools


def memoize(fn):
    known = dict()  # known={}

    @functools.wraps(fn)  # 保留被修饰函数的__doc__ 和签名
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    '''返回前N个数字的和'''
    assert (n >= 0), 'n must be >=0'
    return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    '''返回菲波那切数列的第n个数'''
    assert (n >= 0), 'n must be >=0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    from timeit import Timer

    measuer = [{'exec': 'fibonacci(100)', 'import': 'fibonacci', 'func': fibonacci},
               {'exec': 'nsum(200)', 'import': 'nsum', 'func': nsum}]

    for m in measuer:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {},time: {}'.format(m['func'].__name__, m['func'].__doc__, m['exec'],
                                                                 t.timeit()))
