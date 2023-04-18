

def entreNombres():
    global a
    global b
    a = int(input("A = "))
    b = int(input("B = "))
    while(a <= 2  or a >=b ):
        a = int(input("A = "))
    while(b>=50000):
        b = int(input("B = "))

def checkMersen(i,f):
    n=0
    tr = True
    while(tr):
        if(pow(2,n)-1== i ) :
            tr = False
            f.write(str(i)+"=(2^"+str(n)+")-1,\n")
        else :
            tr =True
            n+=1
        if (n >b):
            tr =False
            
          
def Mersene(f):
    print(a," ",b)
    for i in range(a,b):
       checkMersen(i,f) 

def affichage(f):
    fin_fichier =False 
    while not fin_fichier:
        ligne = f.readline()
        fin_fichier = ligne == ""
        print(ligne)

entreNombres()
f=open("Mersene.txt","w")
Mersene(f)
f.close()
f=open("Mersene.txt","r")

affichage(f)
f.close()
