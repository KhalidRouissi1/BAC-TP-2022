import pickle  
def puis(a,b):
    p=1
    for i in range(b):
       p=p*a
    return p

def premierPuiss(n,x):
    p=1
    i=2
    nb1=0
    nb2=0
    while n!=1 or  x!=1:
   
        while(n % i ==0 ):
           n=n//i
           nb1+=1 
        while(x % i ==0 ):
           x=x//i
           nb2+=1
           print("##########")
      
    
        if(nb1>nb2):
            p=p*puis(i,nb1)
            nb1=0
            nb2=0
        else:
            p=p*puis(i,nb2)
            nb1=0
            nb2=0
        
        i=i+1   
    return  p




def SaisieN():
    global n
    n= int(input("n="))
    while(n<2 or n>100):
        n= int(input("n="))

def RemplireF():
    # f1=open("F_PPCM1.dat","wb")
   
    f= open("F_PPCM.dat","wb") 
    a=0
    b=0
    for i in range(n):
        a= int(input("a="))
        while(a>1000):
            a= int(input("a="))
        b= int(input("b="))
        while(b>1000):
            b= int(input("b="))
        
 
        # ppcm=premierPuiss(a)*premierPuiss(b)
        enere = {}
        enere["a"]=a
        enere["b"]=b
        enere["ppcm"]=premierPuiss(a,b)
        pickle.dump(enere, f)
    f.close()
        
   



def Affichage():
    f=open("F_PPCM.dat","rb") 
    for i in range(n):
            var =  pickle.load(f)
            print("###########################################")
            print(var)
            print("###########################################")
    f.close()

SaisieN()
RemplireF()
Affichage()
