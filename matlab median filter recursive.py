
def medianfilter(
N=2 #median window is 2N+1
window = 2*N +1 #window size
M = 10 #number of data points
x = rand(1, M) #define array size
z = zeros(1,2N+1)#keeps a running set of values for median window

for i in range(N+1,M-N):
    for j in range(1, window):
        z(j) = x(i + j - N - 1)

    median = median(z)#compute median using built in function

functiony = medianfilter(x, 1, N, M)
    
    

