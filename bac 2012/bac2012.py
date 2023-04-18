

from pickle import *


def entree(): 
    global p 
    global n 
    p = int(input("Donner moi la longeur de ton nombre"))
    n = int(input("Donner moi le nombre de ton nombres"))   
    while(n<=2 and n>=100)  :
        n = int(input("Donner moi le nombre de ton nombres"))   
    while(p<=2 or p>= 6):
        p = int(input("Donner moi la longeur de ton nombre"))

def factPrem(x):
    x=int(x)
    i = 2
    ch=""
    
    while(x>1):
        if(x%i == 0 ):
            ch  = ch + str(i)+", "
            x = x // i
        else:
            i=i+1
    return ch[:len(ch)-2]

        
        

def creationNombre(f,f2):
    for i in range(n):
        x = input("Donner moi ton nombre ${}".format(i))
        while(len(x)!=p):
            x = input("Donner moi ton nombre ${}".format(i))
        dump(int(x),f)
        f2.write(factPrem(x)+"\n")
def affichage(f2):
    tr = False 
    while(not tr):
        ligne = f2.readline()
        print(ligne)
        tr = ligne == ""
##
entree()
f=open("Nombre.dat",'wb')
f2=open("facteurs.txt","w")
creationNombre(f,f2)
f.close()
f2.close()
f2=open("facteurs.txt","r")
affichage (f2)
f2.close()