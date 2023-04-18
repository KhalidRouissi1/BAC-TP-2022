

from random import randint


def remplireF(f):
    global n 
    n = int(input("Donner moi le nombre de ligne"))

    while(n>20):
        n = int(input("Donner moi le nombre de ligne max = 20"))
    
    for i in range(n):
        ch=str(randint(0,255))
        for j in range(9):
            ch = ch +" "+ str(randint(0,255))
        f.write(ch+"\n")

    f.close()
    
def tri(m):

    tr =True
    while(tr):
        tr =False
    #     for j in range(10):
    #         for i in range(n):
    #             if(m[j][i]>m[j][i+1]):
    #                 tr =True
    #                 aux = m[j][i]
    #                 m[j][i]=m[j][i+1]
    #                 m[j][i+1] = aux
    # return m

    tr =True
    while(tr):
        tr =False

        for i in range(9):
        
            for j in range(n-1):
                if(m[j][i] >m[j+1][i]):
                    tr=True
                    aux=m[j][i] 
                    m[j][i]=m[j+1][i]
                    m[j+1][i]= aux
    return m
                  
            
        

def remplireM(f,m):
    for i in range(n):
        x= f.readline()
        row=[]
        c=0
        while(x.find(" ")!=-1):
            c+=1
            x=x[x.find(" ")+1:len(x)]
            row.append(int(x[0:x.find(" ")]))
        m.append(row)
    f.close()
    m = tri(m)
def remplireResultat(f2,m):

    for i in range(n):
        ch=""
        for j in range(9):
            ch=ch+" "+str(m[i][j])
        f2.write(ch+"\n")
    f2.close()





f=open("Source.txt","w")
remplireF(f)
f=open("Source.txt","r")
m = []
remplireM(f,m)
f2=open("Resultat.txt","w")
remplireResultat(f2,m)