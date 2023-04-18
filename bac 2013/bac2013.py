

from pickle import * 

def rectangle(n):
    h = (3-0)/n
    s= 0 
    x = 0+h/2
    for i in range(n):
        s = s +( x * x ) *h 
        x = x + h 
    return s 

def trapez(n):
    h = 3/n
    s = 0 
    x = 0 
    for i in range(n):
        s = s +(((x*x )+ ((x+h)*(x+h)))/2)*h
        x = x +h
    return s



def sasireE():
    e = float(input("Donner moi eptillone"))
    while(e<0.001 and e >0.1):
        e = float(input("Donner moi eptillone"))
    return e


def remplireF(e):
    f =open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\bac2013\Calcul.dat","wb")
    n = 0 
    st = 0
    sr = 1
    c={}
    c["Nb"] = []
    c["Mr"]= []
    c["Mt"] = []
   
    while(abs(9-st)>= e and abs(9-sr)>= e):
        n=n+1
        sr = rectangle(n)
        st = trapez(n)
        c["Nb"].append(n)
        c["Mr"].append(sr)
        c["Mt"].append(st)
    dump(c,f)
    f.close()
    print(c)
def affichage ():
    f =open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\bac2013\Calcul.dat","rb")
    
    k = load(f)
    lengthOfAll = len(k["Nb"])
  


    for i in range(lengthOfAll):
        print("Le n est ",k["Nb"][i])
        print("Le Methode Trapez est  ",k["Mt"][i])
        print("Le Methode Rectangle est  ",k["Mr"][i])
        print("--------------------------------")
    if(abs(9-k["Mt"][lengthOfAll-1])<abs(9-k["Mr"][lengthOfAll-1])):
        print("Methode de Trapez converge vers 9 ")
    else:
        print("Methode de Rectangle converge vers 9 ")

    f.close()




e=sasireE()
remplireF(e)
affichage()