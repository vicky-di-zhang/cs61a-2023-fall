# # >>> s = "cs61a"
# # >>> s_iter = iter(s)
# # >>> next(s_iter)
# # Your Answer:
# # c

# # >>> next(s_iter)
# # Your Answer:
# # s

# # >>> list(s_iter)
# # Your Answer:
# # [6,1,a]

# s = [[1, 2, 3, 4]]
# i = iter(s)
# j = iter(next(i))
# print(next(j))
# # 1

# s.append(5)
# print(next(i))
# # 5

# print(next(j))
# # 2

# print(list(j))
# # [3,4]
# print(next(i))
# # StopIteration


# def infinite_generator(n):
#     yield n
#     while True:
#         n += 1
#         yield n
# # print(next(infinite_generator))
# # TypeError: 'function' object is not an iterator
# gen_obj = infinite_generator(1)
# print(next(gen_obj))
# # 1
# print(next(gen_obj))
# # 2
# print(list(gen_obj))
# # [.....]


# def rev_str(s):
#      for i in range(len(s)):
#          yield from s[i::-1]
# hey = rev_str("hey")
# print(next(hey))
# # y
# print(next(hey))
# # e
# print(next(hey))
# # h
# print(list(hey))
# # [y,e]

# def add_prefix(s, pre):
#      if not pre:
#         return
#      yield pre[0] + s
#      yield from add_prefix(s, pre[1:])
# school = add_prefix("schooler", ["pre", "middle", "high"])
# print(next(school))
# # 'preschooler'
# print(list(map(lambda x: x[:-2], school)))
# # ["middleschooler","highschooler"]


##### Q3:
def filter_iter(iterable, f):
    """
    Generates elements of iterable for which f returns True.
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for i in iterable:
        if f(i) == True:
            yield i
            
            
# def differences(it):
#     """ 
#     Yields the differences between successive terms of iterable it.

#     >>> d = differences(iter([5, 2, -100, 103]))
#     >>> [next(d) for _ in range(3)]
#     [-3, -102, 203]
#     >>> list(differences([1]))
#     []
#     """
#     prev = None  
#     for current in it:
#         if prev is not None:
#             yield current - prev
#         prev = current
# d = differences(iter([5, 2, -100, 103]))
# print([next(d) for _ in range(3)])
# list(differences([1]))


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        #else:
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """

    for i in range(n+1,1,-1):
        if is_prime(i):
            yield i

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1 :
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)
    
    
def stair_ways(n):
    """
    Yields all ways to climb a set of N stairs taking
    1 or 2 steps at a time.

    >>> list(stair_ways(0))
    [[]]
    >>> s_w = stair_ways(4)
    >>> sorted([next(s_w) for _ in range(5)])
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
    >>> list(s_w) # Ensure you're not yielding extra
    []
    """
    sum = n
    def helper(sum):
        if sum == 0:
            return [[]]
        elif  sum == 1 :
            return [[1]]
        else:
            r = []
            for step in [1, 2]:
                if sum >= step:
                    for w in helper(sum - step):
                        r.append([step] + w)
            return r
    
    for way in helper(n):
        yield way




    
   