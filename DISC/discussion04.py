def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either one step or two steps at a time.
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(4)
    5
    """
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)
# print(count_stair_ways(1))
# print(count_stair_ways(2))
# print(count_stair_ways(4))

def count_k(n, k):
    """Counts the number of paths up a flight of n stairs
    when taking up to k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0 :
        return 0
    elif n == 0:
        return 1
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n-i,k)
            i += 1
        return total
# print(count_k(3,3))
# print(count_k(4, 4))
# print(count_k(10, 3))
# print(count_k(300, 1))


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1,n) + paths(m,n-1)
               
# print(paths(2, 2))
# print(paths(5,7))    
# print(paths(117, 1))                  
# print(paths(1, 157))  

def max_product(s):
    # 基本情况：如果列表为空，返回1（乘积的恒等元素）
    if not s:
        return 1
    # 如果列表只有一个元素，返回该元素
    elif len(s) == 1:
        return s[0]
    else:
        # 选择包含当前元素的情况：乘以当前元素并跳过下一个元素
        include = s[0] * max_product(s[2:])
        # 选择不包含当前元素的情况：直接递归处理剩余列表
        exclude = max_product(s[1:])
        # 返回两种选择中的最大值
        return max(include, exclude)


# print(max_product([10, 3, 1, 9, 2]))  
# print(max_product([5, 10, 5, 10, 5]))
# print(max_product([]))   

def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6]
    >>> deep                                # input list is unchanged
    [1, [[2], 3], 4, [5, 6]]
    >>> very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
    >>> flatten(very_deep)
    ['m', 'i', 'n', 'm', 'e', 'w', 't', 'a', 't', 'i', 'o', 'n', 's']
    """
    if s == []:
        return []
    else:
        result = []
        for i in s:
            if type(i) == list:
                result += flatten(i)
            else:
                result.append(i)  
    return result

# print(flatten([1, 2, 3]))
# deep = [1, [[2], 3], 4, [5, 6]]   
# print(flatten(deep)) 
# print(deep)
# very_deep = [['m', ['i', ['n', ['m', 'e', ['w', 't', ['a'], 't', 'i', 'o'], 'n']], 's']]]
# print(flatten(very_deep)) 
# print(very_deep)   
 