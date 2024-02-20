class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def sum_nums(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_nums(s.rest)
        

def remove_all(link, value):
    """Removes all nodes in link that contain value. The first element of
    link is never equal to value.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    current = link
    while current.rest is not Link.empty:
        if current.rest.first == value:
            current.rest = current.rest.rest
        else:
            current = current.rest

def flip_two(s):
    """
    Flips every pair of values in s.

    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if s is Link.empty or s.rest is Link.empty:
        return 
    else:
        s.first, s.rest.first = s.rest.first, s.first
        flip_two(s.rest.rest)



def make_circular(s):
    """Mutates linked list s into a circular linked list.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> make_circular(lnk)
    >>> lnk.rest.first
    2
    >>> lnk.rest.rest.first
    3
    >>> lnk.rest.rest.rest.first
    1
    >>> lnk.rest.rest.rest.rest.first
    2
    """
    if s is Link.empty:  
        return
    head = s 
    while s.rest is not Link.empty: 
        s = s.rest
    s.rest = head  
    
        

