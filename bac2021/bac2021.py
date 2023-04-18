# eneregistrement t  =Hex Num Dec  fiche ImgHexa.txt



def ConvertDec(x):
    s=0

    for i in range(len(x)):
        if ("0">= x[i] or x[i]<="9"):
            y= int(x[i])
        else:
            y = ord(x[i])-55
        s = s +y* pow(16,len(x)-1-i)
     
    return s
def trie(t):
    tr = True
    while tr:
        tr=False
        for i in range(0,len(t)-1):
            if(t[i]['Dec']>t[i+1]['Dec']):
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                tr = True
    return t






    
def RemplireT(f):
    t=[]
    i=0
    tr=True
    n=0
    while(tr):
        x = f.readline()
        n+=1
        tr = not(x=="")
    f.close()
    f=open("ImgHexa.txt","r")
    
    for i in range(n-1):
        enre={}
        x = f.readline()
        i+=1
     
        x=x[:len(x)-1]
        enre["Hex"]=x
        enre["Num"]=i
        enre["Dec"]=ConvertDec(x)
        t.append(enre)
    return trie(t)


def Genere(Nb):
    mot=""
    while(Nb!=0):
        r=Nb % 3 
        if(r ==0):
            Y="Ma"
        elif(r==1):
            Y="Des"
        else:
            Y="Son"
        Nb=Nb//3
        mot = Y+mot
    return mot


def RemplireR(f1,t):
    for i in range(len(t)):
        f1.write(Genere(t[i]["Dec"])+" "+str(t[i]["Num"])+"\n")

















f=open("ImgHexa.txt","r")

t=RemplireT(f)
print(t)
f.close()
f1=open("Resultat.txt","w")

RemplireR(f1,t)
f1.close()