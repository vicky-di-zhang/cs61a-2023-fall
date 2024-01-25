def search(f):   # search the "x" (from 0 to infinity) that make f(x) is true
    x = 0
    while not f(x):
        x += 1
        #print(x)
    return x

def is_three(x):
    return x==3

#print(search(is_three))

def square(x):
    return x*x

def positive(x):
    return max(0,square(x)-100)
# when x > 10, then start to return >0

# print(search(positive)) # 11

def inverse(f):  # get f, return a function that figure out the x which after f(x) == y
    return lambda y : search(lambda x : f(x) == y)

print(inverse(square)(256))
a = inverse(square)
print(a(169))




