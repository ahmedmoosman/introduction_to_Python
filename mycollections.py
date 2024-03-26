def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.
    
    par n: integer
    out  : list
    """ # the function help
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        #  better than print(a), why?
        a, b = b, a+b


