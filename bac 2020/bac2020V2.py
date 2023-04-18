from pickle import * 

def Divis13(n):
    n = str(n)
    while (len(n) % 3 != 0 ):
        n = "0"+n
    unite = n[len(n)-1]
    number = n[0:len(n)-1]
    
    if ((int(number)+4*int(unite) )% 13 == 0 ):
        return True
    else:
        return False


def Divis7(n):
    n = str(n)
    while (len(n) % 3 != 0 ):
        n = "0"+n
    s=0
    signe = 1

    while (len(n) !=0):
        k=n[len(n)-3:len(n)]
        
        s=s+int(k[len(k)-1])*1*signe + int(k[len(k)-2])*3*signe  + int(k[len(k)-3])*2*signe  
        signe = -signe
        n = n [0:len(n)-3]
    newS = 0
    if (s == 7 or s == 0 ):
        return True
    else:
        if(len(str(s))!=1):
            s = str(s)
            newS = int(s[1])  * 1 + int(s[0]) * 3   
            if ( newS == 7 or newS == 0):
                return True
            else : 
                return False
        else :
            return False


def SasireNb():
    nb= int(input("Donner moi nb "))
    while nb <  5 :
        nb= int(input("Donner moi nb "))
    return nb

def RemplireNb(nb):
    Nombre = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Nombre.dat","wb")
    ch =""
    for i in range(nb):
        x = int(input("Donner moi ton nombre"))
        dump(x,Nombre)
    Nombre.close()




def PlacerNobres(nb):
    Nombre = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Nombre.dat","rb")
    Div13 = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Div133.txt","w")
    Div7 = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Div77.txt","w")   
    for i in range(nb):
        x = load(Nombre)
        if (Divis13(x)):
            print("Ssssqsdqdqsdqsd")
            Div13.write(str(x)+"\n")
        if (Divis7(x)):
            print("-----------------------------------------------------------------------------------")
            Div7.write(str(x)+"\n")
    
    
    
    Nombre.close()
    Div13.close()
    Div7.close()





nb=SasireNb()
RemplireNb(nb)
PlacerNobres(nb)
