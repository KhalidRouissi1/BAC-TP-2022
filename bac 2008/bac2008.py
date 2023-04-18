
from pickle import *



def sasirN():
    n= int(input("Donner moi n "))
    while n>=10 or n >=100:
        n= int(input("Donner moi n "))
    return n 




def rempliref1(n,f):
    
    for i in range(n):
        x=int(input(f"Donner moi ton {i} nombre"))
        while(x>32000):
            x=int(input(f"Donner moi ton {i} nombre"))
        dump(x,f)



def verifieEtRemplire(n,f,f1,f2):

    for i in range(n):
        x = load(f)
        k=x
        ch =""
        while(k!=0):
            r = k%2
            k = k // 2
            ch = str(r) + ch
        z = 0
        u = 0         
        for i in range(len(ch)):
            if ch[i]=="0":
                z+=1
            else:
                u+=1
        if z >u : 
            dump(x,f2)
            print(x)

        else:
            dump(x,f1)
        




f=open("naturels.dat","wb")
n = sasirN()
rempliref1(n,f)
f.close()
f=open("naturels.dat","rb")
f1=open("rond.dat","wb")
f2=open("non_rond.dat","wb")
verifieEtRemplire(n,f,f1,f2)


f1.close()
f2.close()
f.close()
