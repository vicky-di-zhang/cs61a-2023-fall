from math import gcd
#Q1:
def make_rat(num, den):
    """Creates a rational number, given a numerator and denominator.

    >>> a = make_rat(2, 4)
    >>> numer(a)
    1
    >>> denom(a)
    2
    """
    return [num,den]

def numer(rat):
    """Extracts the numerator from a rational number."""
    g = gcd(rat[0], rat[1])
    return rat[0] // g

def denom(rat):
    """Extracts the denominator from a rational number."""
    g = gcd(rat[0], rat[1])
    return rat[1] // g

#Q2:
def div_rat(x, y):
    """The quotient of rationals x/y.
    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> numer(c)
    9
    >>> denom(c)
    20
    """
    g = gcd (x[0] * y[1],x[1] * y[0])
    return [x[0] * y[1] // g, x[1] * y[0] // g]

#Q3:
def lt_rat(x, y):
    """Returns True if x < y as rational numbers; else False.
    >>> a, b = make_rat(6, 7), make_rat(12, 16)
    >>> lt_rat(a, b)
    False
    >>> lt_rat(b, a)
    True
    >>> lt_rat(a, b)
    False
    >>> a, b = make_rat(-6, 7), make_rat(-12, 16)
    >>> lt_rat(a, b)
    True
    >>> lt_rat(b, a)
    False
    >>> lt_rat(a, a)
    False
    """
    return (x[0] * y[1] - x[1] * y[0]) < 0

# a = make_rat(2, 4)
# print(numer(a))
# print(denom(a))

# a, b = make_rat(3, 4), make_rat(5, 3)
# c = div_rat(a, b)
# print(numer(c))
# print(denom(c))

# a, b = make_rat(6, 7), make_rat(12, 16)
# print(lt_rat(a, b) == False)
# print(lt_rat(b, a)==True)
# print(lt_rat(a, b)==False)
# a, b = make_rat(-6, 7), make_rat(-12, 16)
# print(lt_rat(a, b)==True)
# print(lt_rat(b, a)==False)
# print(lt_rat(a, a) == False)




#Q4:
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the tree's list of branches is empty, and False otherwise."""
    return not branches(tree)



# t2 = tree(3,
#         [tree(4),
#          tree(5),
#          tree(6)])

# t1 = tree(1,
#         [t2,
#          tree(2)])

# t = tree(1, [tree(2), tree(4)])

# label(t) : 1
# t[0]: 1
# label(branches(t)[0]) : 2
# is_leaf(t[1:][1]) : is_leaf(branches(t)[1]) : 4
# [label(b) for b in branches(t)] : [2, 4]
# branches(tree(5, [t, tree(3)]))[0][0]: label(branches(tree(5, [t, tree(3)]))[0]) : 1


# Q5:
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    if is_leaf(t):
        return 0
    elif len(branches(t)) == 1:
        return 1 + height(branches(t)[0])
    else:
        return 1 + max(height(branches(t)[0]),height(branches(t)[1]))


# # t = tree(3, [tree(5, [tree(1)]), tree(2)])
# # print(height(t) == 2)
# # t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
# # print(height(t)==3)

# #Q6:
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if is_leaf(t) or label(t) == x:
        return ([x] if t == x or label(t) == x else None)
    for b in branches(t):
        path = find_path(b,x) 
        if path:
            return [label(t)] + path
        
# t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
# print(find_path(t, 5) == [2, 7, 6, 5])
# print(find_path(t, 10))





# #  Q7:
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t),[tree(x) for x in leaves])
    else:
        new_branches = [sprout_leaves(b, leaves) for b in branches(t)]
        return tree(label(t),new_branches)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
           
t1 = tree(1, [tree(2), tree(3)])
print_tree(t1)
new1 = sprout_leaves(t1, [4, 5])
print_tree(new1)
t2 = tree(1, [tree(2, [tree(3)])])
print_tree(t2)
new2 = sprout_leaves(t2, [6, 1, 2])
print_tree(new2)


def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    return int(label(t)) + sum([sum_tree(b) for b in branches(t)])

            
# t = tree(4, [tree(2, [tree(3)]), tree(6)])
# print(sum_tree(t))


def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    # if is_leaf(t):
    #     return True
    # first_branch_sum = sum_tree(branches(t)[0])
    # for b in branches(b):
    #     if sum_tree(b) != first_branch_sum:
    #         return False
    # return True
    return  all([sum_tree(b) == sum_tree(branches(t)[0]) and balanced(b) for b in branches(t)])
## all([]) is true


t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
print(balanced(t))
t = tree(1, [t, tree(1)])
print(balanced(t))
t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
print(balanced(t))
print(all([]))
