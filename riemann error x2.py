'''
program to obtain area under x^2 curve using riemann sum method. also calculates
area correct to given error value.
'''


import math
import matplotlib.pyplot as plt

def midpoint_riemann_sum(n, a, b, error):
    interval_length = float(b - a)
    dx = interval_length / n
    
    riemann_sum = 0
    
    for i in range(n):
        riemann_sum += f(a + dx/2 + i*dx)
    riemann_sum *= dx

    return riemann_sum

def c_error(a, b, n, error):
    
    int_old = midpoint_riemann_sum(n, a, b, error)
    int_new = midpoint_riemann_sum(2*n, a, b, error)
    c_e =  abs(int_old - int_new)
    
    while c_e>error:
        n*=2
        int_old = int_new        
        int_new = midpoint_riemann_sum(2*n, a, b, error)      
        c_e =  abs(int_old - int_new)

        print('int_old =',int_old)
        print('int_new =',int_new)
        print("C-Error = ", c_e)
        
    return int_old
    
def f(x):
    try:
        y = x**2
    except ZeroDivisionError:
        y = 0
    return y

def run():
    n = int(input("Please enter number of intervals = "))
    a = int(input("Please enter value of a = "))
    b = int(input("Please enter value of b = "))
    error = float(input("Please enter value of error = "))

    #Riemann Sum
    riemann_sum = c_error(a, b, n, error)
    print('Riemann Sum =' , riemann_sum)

    
run()
