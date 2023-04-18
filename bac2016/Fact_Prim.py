

def premier(c):
    k=0
    for i in range(1,c):
        if c % i ==0:
            k+=1
    return  k <2


def SasieN():
    global n 
    n=int(input("N="))
    while(n<2 or n>5):
        n=int(input("N="))
    global t
    t=[]
    for i in range(n):
        k=int(input("Donner moi un nombre"))
        t.append(k)

def fact(x):
    f= x
    for i in range(1,x):
        f =f*i
    return f


def PF(x):
    tr=False
    i=0
    while(fact(i)<x):
        i+=1
        if((fact(i)+1 == x) or (fact(i)-1 == x)):
            tr = True 
    return tr 


def PP(x):
    tr=False
    prem = 1
    i=0
    while(prem+1<x and prem-1<x):
        i=i+1
        if(premier(i)):
            prem = prem * i
        if(prem+1 == x or prem-1 == x):
            tr = True 
    return tr 



def arithmetique():
    pf=""
    pp=""
    for i in range(n):
        if(PF(t[i]) and premier(t[i])):
            pf = pf +str(t[i])+","
        if(PP(t[i]) and premier(t[i])):  
            pp = pp +str(t[i])+","
    print(pf[:len(pf)-1])
    print(pp[:len(pp)-1])


if(PF(719) and premier(719)):
    print(str(719))

if(PF(7) and premier(7)):
    print(str(7))


if(PP(7) and premier(7)):
    print(str(7))

SasieN()
arithmetique()