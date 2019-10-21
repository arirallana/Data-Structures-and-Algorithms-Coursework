'''
This program implements the extended euclid's algorithm to return the
greatest common divisor of two numbers m and n as :
gcd = m*a +n*b, where a and b are integers
'''


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    print("gcd = ", gcd, "\n", "a = ", x, "\n", "b = ", y)
    return gcd, x, y

egcd(1769,551)
