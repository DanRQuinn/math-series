def fibonacci(n):
    """Return the nth idx in fibonacci sequence"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):
    """Return the nth idx in lucas sequence"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
def sum_series(n, param1=0, param2=1):
    """Return the nth element of a recusive summation series with optional paramaters
    param1: optinal first param, 1st in sequence def-value: 0
    param2: optional second param, 2nd in sequence def-value: 1
    
     """
    if n == 0:
        return param1
    elif n == 1:
        return param2
    else:
        return sum_series(n-1, param1, param2) + sum_series(n-2, param1, param2)


# if param1 is equal to 0 = fibonnaci
# and
# param2 is equal to 1 = fibonnaci
# if param1 == 0,1 then fibonacci
# if param2 == 2,1 then lucas

