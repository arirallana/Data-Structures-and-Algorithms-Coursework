'''
Euclid's Algorithm for finding the greatest common divisor of two terms m and n. 
'''


def euclid(m,n):
    rem = m % n
    if rem == 0:
        print("gcd = " + str(n))
        return n
    
    else:
        m = n
        n = rem
        return euclid(m, n)

def run():
    m = int(input("Please enter first number"))
    n = int(input("Please enter second number"))
    euclid(m,n)

run()
        
