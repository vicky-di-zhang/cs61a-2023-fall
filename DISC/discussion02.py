'''
# draw the environment diagram!!!! result is x = 21
# very tricky. Remenber: if you need something, find it from this framework or last
#              dont "think it for granted".
# if you forget how to finish it: https://www.bilibili.com/video/BV138411F7vT?p=51&vd_source=8dcf087f62ffdb64351118000a13f13e

a = lambda x: x * 2 + 1
def b(b, x):
    return b(x + a(x))
x = 3
x = b(a, x)

# draw the environment diagram!!!! result is 19
# # very tricky. be careful :the symbol of n and k 
n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)
'''


def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    def check(cond):
        begin = 1
        end = n
        while begin <= end:
            if cond(begin):
                print(begin)
            begin += 1
    return check


from operator import add, mul, mod
def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    def deep(x):
        def deeper(y):
            return func(x,y)
        return deeper
    return deep

# print(curry(mod)(123)(10))


def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x : x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda : lambda x : lambda : x


# extra practice
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
'''
    def helper(x):
        ____________________________
        while ____________________________:
            if ____________________________:
                return ____________________________
            ____________________________
        ____________________________
    return helper
'''

### not finish

def match_k(k):
    def helper(x):
        num_digit = 0
        num_x = x
        num_xx =x  
        while num_x>0 :
            num_x //= 10
            num_digit += 1
        a = num_digit
        print(a)

        while num_digit >-1:
            pow = num_digit-1
            x = num_xx
            while pow > -1:
                if (x // (10**pow)) !=((x // (10**(pow-k)))%10):
                    print(pow,(x // (10**pow)) )
                    return False
                pow -= k
            num_digit -= 1
        return True
    
    return helper


print(match_k(3)(123123))





