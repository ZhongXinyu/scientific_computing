"""
This programmes helps to find the value of sqrt(x) using the method of bisection.

To find the square root value of c, we are finding the solution to the value of f(x)=c-x^2=0.

"""
import numpy as np

def bisection(func,n):
    lower_bound,upper_bound=0,n
    while abs(upper_bound-lower_bound)>=10**(-7):
        test=(upper_bound+lower_bound)/2
        if func(test)*func(lower_bound)>=0:
            lower_bound=test
        else:
            upper_bound=test
    return test

n=int(input("Please input a number: "))
print (f'The square root value of {n} is {bisection(lambda x: n-x**2,n)}')