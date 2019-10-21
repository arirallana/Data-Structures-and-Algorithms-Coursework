'''
program to calculate the area under any given curve of function f(x) using riemann sum
approximation. 
'''

import math
import matplotlib.pyplot as plt

def midpoint_riemann_sum(n, N):
    a = -N/2
    b = (N/2)-1
    interval_length = float(b - a)
    dx = interval_length / n
    
    riemann_sum = 0
    
    for i in range(n):
        riemann_sum += f(a + dx/2 + i*dx)
    riemann_sum *= dx

    return riemann_sum

def f(x):
    try:
        y = ((math.sin(x))/x)
    except ZeroDivisionError:
        y = 0
    return y

def run():
    n = int(input("Please enter number of intervals"))
    N = int(input("Please enter value of N"))

    #Riemann Sum
    riemann_sum = midpoint_riemann_sum(n, N)
    print(riemann_sum)

run()
