def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m,n-1)

print(multiply(5,3))


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n == 1:
        return False
    elif n == 2 :
        return True
    else: 
        def divi(x,y):
            if  y < 2:
                return True
            else:
                return (not (x%y == 0)) and divi(x,y-1)
        return divi(n,n-1)
    
    
print(is_prime(1))
print(is_prime(2))
print(is_prime(521))
print(is_prime(16))


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    def print_count(x):
        print(x)
        if x == 1:
            return 1
        elif x%2 == 0:
            return 1 + print_count(x//2)
        elif x%3 != 0:
            return 1 + print_count(x*3+1)
    return print_count(n)

a = hailstone(10)
print(a)
