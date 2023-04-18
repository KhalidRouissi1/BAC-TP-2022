
from pickle import *
from random import randint, random 


def sasirN():
    n= int(input("Donner moi ton nombre"))
    while(n<=2 or n >50):
        n= int(input("Donner moi ton nombre"))
    return n

def remplireFiche(n,f):
    for i in range(n):
        dump(randint(1,9),f)
def triMin(t,n):
    tr = True
    while(tr):
        tr = False
        for i in range(n-1):
            if(t[i]>t[i+1]):
                aux = t[i]
                t[i]=t[i+1]
                t[i+1]= aux
                tr= True
    ch =""
    for i in range(len(t)):
        ch = ch +str(t[i])
    return ch

def triMax(x):
    if len(x)==0:
        return ""
    else:
        return x[len(x)-1] + triMax(x[0:len(x)-1]) 

def readFromF(f,n):
    #Reading and appending
    fin_fichier =False
    t=[] 
    while not fin_fichier:
        try:
            e=load(f)
            t.append(e)
        except:
                fin_fichier = True
    
    global pn 
    global gn
    pn=triMin(t,n)
    gn= triMax(pn)

def affichage():
    l = len(gn)//2
    r=0
    s=0
    k=[]
    for i in range(l):
        s = int(gn[r]) - int(gn[len(gn)-1-r])
        r=r+1
        k.append(s) 
    print(k)
    r = k[1]-k[0]
    i = 3
    while(i<=l and k[i]-k[i-1]==r ):
        i=i+1
    if(i>l):
        print("Le chiffre de gn froment une suite arithmetique de raison ==${}".format(r))  
    else:
        print("Le chiffre de gn n'est froment pas une suite arithmetique ")  

n=sasirN()
f=open("Nombre.dat","wb")
remplireFiche(n,f)
f.close()
f=open("Nombre.dat","rb")
readFromF(f,n)
f.close()
affichage()