from pickle import *

def CalculTerm(u0):

    i=0
    while u0 != 1:
        if(u0 % 2==0):
            u0= u0 // 2
            i+=1
            
        else:
            u0= 3*u0+1
            i+=1    
           

    return i



def remplireDepart(f):
    global p
    p=int(input("P="))
    while(p<2 or p>1000):
        p=int(input("P="))
    
    for i in range(p):
        nb = int(input("Donner moi to nombre"))
        while(nb<2):
            nb = int(input("Donner moi to nombre"))
        dump(nb,f)
    f.close()


def remplireSuite(f,f2):
    enre={}
    for i in range(p):
        u0=load(f)
        enre["Dep"]=u0
        enre["Nb"]=CalculTerm(u0)
        dump(enre,f2)

    f.close()


def affichage(f2):
    x=load(f2)
    m=x["Nb"]
    
    for i in range(1,p):
        x=load(f2)
        if x["Nb"] <m :
            m=x["Nb"]
            e=x["Dep"]
    print("U0={} de nombre de terme = {}".format(e,m))
    f2.close()

f = open("Depart.dat","wb")
remplireDepart(f)
f = open("Depart.dat","rb")
f2=open("Suite.dat","wb")
remplireSuite(f,f2)
f2=open("Suite.dat","rb")
affichage(f2)