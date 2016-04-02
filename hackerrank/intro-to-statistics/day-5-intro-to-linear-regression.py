#! /bin/python3

math = 95, 85, 80, 70, 60
stats = 85, 95, 70, 65, 70

def least_squares(X, Y):
    n = len(X)
    assert n == len(Y)
    xy = [ x * y for x, y in zip(X, Y)]
    xx = [ x ** 2 for x in X ]
    b = (n * sum(x * y for x, y in zip(X, Y)) - sum(X) * sum(Y)) / (n * sum(x**2 for x in X) - sum(X)**2)
    a = (sum(Y) - b * sum(X)) / n 
    return a, b

def predict(x, a, b):
    return a + b * x

a, b = least_squares(math, stats)
print(predict(80, a, b))
