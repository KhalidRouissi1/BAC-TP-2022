




from cmath import sqrt

def Rep_Binary(x,n):
    cn="0."
    for i in range(1,n+1):
        if 2* x < 1:
            cn = cn + "0"
            x = x *2
        else:
            cn=cn +"1"
            x = 2*x-1
    return cn
# print(Rep_Binary(0.825,5))






def valeur2():
    sp1 = 1/5
    sp2 =1/239
    i = 3
    pp = 0
    pa = 1
    signe = -1
    while(abs(pa-pp)>= 0.0001):
        sp1 = sp1 + (1/i *(1/5**i)*signe)
        sp2 = sp2 + (1/i * 1/239**i * signe)
        signe = - signe
        i+=2
        pp = pa 
        pa = (16*sp1) - (4*sp2)  
        print(pa)

    return pa 

# print(valeur2())

def pi(n):
    h = (1)/n
    s=0
    # x= 0 Gauche 
    # x= 0 + h  Droit 
    # x = (0+h)/2 meluie
    x = (0+h)/2

    for i in range(0,n):
        s= s + (sqrt(1-x**2) * h)
        x = x+ h

    return 4*s
# print(pi(4))

def pi_trapez(n):
    h = (1)/n
    s=0
    # x= 0 Gauche 
    # x= 0 + h  Droit 
    # x = (0+h)/2 meluie
    x = (0+h)/2

    for i in range(0,n):
        # s= s + (sqrt(1-x**2) * h)
        s= s +((sqrt(1-x**2) + sqrt(1-x**2)+h) * h/2)
        x = x+ h

    return 4*s

# print(pi_trapez(5))



def conv_10(x):
    while len(x) % 2 != 0 :
        x = "0" + x
    ch =""
    while len(x) != 0 :
        k = x[0:3]
        s =  0
        for i in range(len(k)):
            s = s + int(k[i]) * pow(2,len(k)-1-i)
        ch = ch + str(s)
        x = x[3:len(x)]
    return ch

# print(conv_10('10110'))



def conv_810(x):
    while(len(x)% 8 != 0 ) :
        x = "0"+x
    print(x)
    ch = ""
    while(len(x)!=0):
        k = x[0:8]
        s= 0 
        for i in range(len(k)):
            s = s + int(k[i])* (2**(len(k)-1-i))
        print(ch)

        ch = ch + chr(s)
        x = x[8:len(x)]


    return ch 
# print(conv_810("010000100110111101101110"))
# 01101111   01101110


def toBinary(n,b):
    ch=""
    while(n != 0):
        r = n % b 

        n = n // b 
        if(r <= 9): 
           ch = str(r) + ch 
        else:
            ch = chr(55 +r) + ch

    
    return ch
# print(toBinary(74,16))





def puissance(x,y):
    k = 1
    for i in range(y):
        k =  k *x

    return k

print(puissance(100,5))





def premier(n):
    k=0
    tr = True
    while tr:
        for i in range(1,n):
            if (n%i == 0 ):
                k+=1
            else :
                tr = False
        if (k==1):
            tr = True
        else:
            tr=False
        return tr 
# print(premier(2))

def real_premier(n):
    i=2
    k=''
    while n > 1 :
        if n % i == 0 :
            n = n // i
            k = k+str(i)
        else:
            i =i +1
    return k 

# print(real_premier(25))

def point_fixe():
    sp=0
    sa =1 
    i = 0
    while(abs(sa-sp)>=0.0001):
        sp = sa
        sa = sa/2
    return f"Le point fixe est {sa} et letteration est{i}"
