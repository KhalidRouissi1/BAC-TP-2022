

def f(x):
    return 1/((1+x)*(1+x))
def trapez (a,b,n):
    s= 0 
    h = (b-a)/n
    x = a 
    for i in range(1,n):
        s = s + ((f(x)+f(x+h))/2)*h
        x =x +h
    return s

def approximation(a,b):
    n=0
    rp=0
    ra=1
    while(abs(ra-rp) >= 0.001):
        n =n+1
        rp = ra
        ra = trapez(a,b,n)
    return ra
print(approximation(0,1))
