'''
# None,0,False,"",{},[],():   all are False
# everything else : True

# not : always return either True or False
>>> not None 
True
>>> not True
False
>>> not -8  # not True
False
>>> not ""
True

# and : evaluates expressiong in order;  
#       stops evaluating at the first falsy value and return it 
#       if all values evaluate to a truthy value, the last value is returned

>>> -1 and 0 and 1
0
>>> "i" and "love" and "cs" and "61a"
"61a"

# or : evaluates expressiong in order;  
#      stops evaluating at the first truthy value and return it.(even 1/0 could make an error,but doesnt matter, wont excuted)
#      if all values evaluate to a falsy value, the last value is returned

>>> False or 9999 or 1/0
9999

# if-elif-else: check if-eilf condition in order,
#               choose one of them to excuted then end the block
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

# special_case() = 12


# every if-elif-else is block: excuted one of them then jump out of block
              if is necessary, elif-else arent.
              every block start with if
def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

# just_in_case() = 19


# return is exit of function: function will be jumped out/stopped by encounting the first "return"
                 and not counitue to excute the rest code
def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

# case_in_point() 12

'''

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    
    "*** YOUR CODE HERE ***"
    if temp < 60 or raining:
      return True
    else:
      return False
print(wears_jacket_with_if(90, False)  )
print(wears_jacket_with_if(40, False)  )
print(wears_jacket_with_if(100, True)  )


def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    if n%10 <= 4:
      return (n-n%10)
    else:
      return (n+10-n%10)

print(nearest_ten(0))
print(nearest_ten(4))
print(nearest_ten(5))
print(nearest_ten(61))
print(nearest_ten(2023))


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i<=n :
      if i%5 == 0 and i%3 == 0:
        print("fizzbuzz")
      elif i%5 == 0 :
        print("buzz")
      elif i%3 == 0 :
        print("fizz")
      else:
        print(i)
      i += 1

      
print(fizzbuzz(16))

# prime: divided by [2,n-1]. (not 1 and not n)
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
      return  False
    
    k = 2
    while k < n :
        if n%k == 0:
          return False
        k += 1
    
    return True

print(is_prime(1))
print(is_prime(7))  
print(is_prime(10))    
     
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    if 0<n<10:
      return 1
    else:
      num_digit = 0
      num_same = 0
      while n > 0:
        num_same += has_digit(n//10, n%10)
        num_digit += 1
        n //= 10
    return (num_digit-num_same)
'''
#method 1:
    unique_counter = 0
    while n!= 0:
       if not has_digit(n//10, n%10):
         unique_counter += 1
       n //= 10
    return unique_counter
  
#method 2: all the unique numbers are just:0,1,2,3,4,5,6,7,8,9.
#       That means unique_counter is maximum 10(0~9),so we just need to check how many number n has in (0~9)
  i = 0
  unique_counter = 0
  while i<10:
    if has_digit(n, i):
      unique_counter += 1
    i += 1
  return unique_counter
  
   
  
  
    
'''
        
        

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    result = False
    while n >0 and result == False:
      if n%10 != k:
          n //= 10
      else:
          result = True
    return result
    '''
    while n != 0 :
      if n%10 == k:
         result = True
      n //= 10
    return False
    '''

print(unique_digits(8675309))
print(unique_digits(13173131))
print(unique_digits(10))

print(has_digit(10, 1))
print(has_digit(1, 1))
print(has_digit(5,1))
print(has_digit(12,7))

print(False or True or 1/0)