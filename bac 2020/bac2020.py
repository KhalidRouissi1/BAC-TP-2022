

def Divis13(n):
    n  = str(n)
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
        s =s+int(k[len(k)-1])*1*signe + int(k[len(k)-2])*3*signe  + int(k[len(k)-3])*2*signe  
        signe = -signe
        n = n [0:len(n)-3]
    newS = 0
    if (s == 7 or s == 0 ):
        return True
    else:
        s = str(s)
        newS = int(s[1])  * 1 + int(s[0]) * 3   
        if ( newS == 7 or newS == 0):
            return True
        else : 
            return False




def SasirNb(nb):

    nb= int(input("Donner moi nb "))
    while nb <  5 :
        nb= int(input("Donner moi nb "))
    
    Nombre = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Nombre.txt","w")
    ch =""
    for i in range(nb):
        x = input("Donner moi ton nombre")
        ch = ch+ x +"\n"
    Nombre.write(ch)
    Nombre.close()


Nombre = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Nombre.txt","r")
Div13 = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Div13.txt","a")
Div7 = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac 2020\Div7.txt","a")
def PlacerNobres(nb,Nombre,Div13,Div7):
    x =""
    for i in range(nb):
        x = Nombre.readline()
        print(i)
        if (Divis13(x)):
            Div13.write(x+"\n")
        if (Divis7(x)):
            Div7.write(x+"\n")
    Nombre.close()
    Div13.close()
    Div7.close()


nb=0
SasirNb(nb)
PlacerNobres(nb,Nombre,Div13,Div7)