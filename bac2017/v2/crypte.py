from random import randint


def SasieCle():
    global n 
    n =int(input("n="))
    while n<5 or n >10:
        n =int(input("n="))
    global cle
    cle=""
    
    for i in range(n):
        random = randint(1,25)

        cle = cle+(chr(random + 65))

def getLength(f):
    f=open("Source.txt","r")

    counter=0
    fin=False
    while not(fin):
        x=f.readline()
        fin =x== ""
        counter=counter+1
    f.close()
    return counter 




def crypte(f,f2):
    global m
    m=[]
    fin_fiche=False
    while not(fin_fiche):
        ligne = f.readline()
        x= ligne
        fin_fiche = ligne == ""
        while(len(x) % len(cle) !=0):
            x = x +" "
            # c= len(cle)
  

        m=[]
        tr=True
        while(x !=""):
            # l=l+1
            row = []
            z =x[0:len(cle)]
            for j in range(len(z)):
                r=z[j]
                if(r=="\n"):
                    r = " "
                row.append(r)
                    
            m.append(row)
            x = x[len(cle):]
      
        ch =""
        if(len(m)!=0):

            for i in range(3):
                ch1=""
                for j in range(len(m)):
                    ch1 = ch1 +m[j][i]
                ch = ch+cle[i]+ch1
            f2.write(ch+"\n")
 













SasieCle()
f=open("Source.txt","r")
f2=open("Crypt.txt","w")
crypte(f,f2)
f.close()
f2.close()
