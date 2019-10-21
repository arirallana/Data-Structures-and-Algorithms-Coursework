'''
This program plots any given function f(x) (in this case sin(x)/x) and it's
fourier transform.

'''



import math
import matplotlib.pyplot as plt

def f(x):
    try:
        y = ((math.sin(x)/x))
    except ZeroDivisionError:
        y = 1
    return y

def fourier_transform(N, X):

    x = []
    y = []
    u = []
    F = []
    
    for i in range(1, N+2):
        x.insert(i-1, 0)
        y.insert(i-1, 0)
        
    dx = X/N
    dw = 2*math.pi/N

    for m in range(1, N+2):
        u_m = dw*(m-(N/2)-1);
        u.append(u_m)
        
        RiemannSum = 0;
        for n in range(1, N+2):
            
            x_n = dx*(n-(N/2)-1)
            x.insert(n-1,x_n)
            x.pop()
            
            y_n = f(x_n)
            y.insert(n-1,y_n)
            y.pop()
            
            v_n = y_n*math.cos(u_m*x_n)*dx
            
            RiemannSum = RiemannSum + v_n
            
        F.append(RiemannSum)

##    print(x)
##    print(y)
##    print(u)
##    print(F)
    
    plot_(x,y,u,F)


def plot_(x, y, u, F):
    plt.plot(x,y, label='sin(x)/x')
    plt.plot(u,F, label='F(w)')
    plt.title('Fourier Transform')
    plt.legend()
    plt.show()


fourier_transform(4000,32)
    
