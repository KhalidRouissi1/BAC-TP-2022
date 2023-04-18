def sasirN():
    n=int(input("Donner moi ton n"))
    while (n>=4000 and n <=100000):
        n=int(input("Donner moi ton n"))

    return n

def premier(x):
    dv=0
    x =int(x)
    tr=True
    for i in range (1,x+1):
        if(x%i == 0 ):
            dv+=1
    
    if(dv>2):
        tr= False
    return tr        
        
def Sup_Prem(x):
    x=str(x)
    k=0
    while(len(x)>0):
        if (premier(x)):
            x=x[0:len(x)-1]
        else:
            k=k+1
            x=x[0:len(x)-1]
    if (k==0):
        return True
    else:
        return False
def remplire(n,f):
    x=1
    while(x<n):
        print(x)
        if(Sup_Prem(x)):
            f.write(str(x)+"\n")
            print(x)
            x=x+1
        else:
            x=x+1
            




f=open("sup_prem.txt","w")

n=sasirN()
remplire(n,f)
f.close()