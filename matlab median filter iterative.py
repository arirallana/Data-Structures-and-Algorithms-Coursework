N = 2        # median window is 2N+1
Window = 2*N+1  # Window size
M = 100      # total number of data points
x =  rand(1,M)   # define array size
x1 = zeros(1,M) 
z1 = zeros(1,M)
z = zeros(1,2*N+1);% keeps a running set of values for median window
for i = 1:M
    x(i) = cos(i*pi()/10) + 0.4 * x(i)
end
for i = 1+N:M-N
    for j = 1:Window
    z(j) = x(i+j-N-1)
    end  
    medianz = median(z) # compute the median of points in window z
    x1(i) = x(i)
    z1(i) = medianz
    disp (z1)
end

Figure([x1',z1']) 
