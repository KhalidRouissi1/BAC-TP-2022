
### Entre le mot cle 
### Remplire le matrice 
### Remplire Le fichier crypte 

from numpy import * 

def lengthOfFile():
    f = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac2017\source.txt","r")
    return len(f.readlines())



def RemplireMat(cle):
    f = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac2017\source.txt","r")
    
    
    for i in range(lengthOfFile()) : 
        m=[]
        k=f.readline()

        while(len(k) % len(cle) != 0):
            k= k +" "

        while (k !=""):
            row = []
            for c in range(0,len(cle)):
                s = k[c]
                if s =='\n':
                    s = " "
                row.append(s)
            k=k[c+1:len(k)]
            m.append(row)
       
        print(m)

        f2 = open(r"E:\EasyPHP-5.3.6.1\www\STI2019\bac2017\crypte.txt","a")
        bigch=""
        for rr in range(len(cle)):
            ch=""
            bigch = bigch + cle[rr] 

            for r in range(len(m)):
                ch  = ch+m[r][rr]
            bigch = bigch+ ch
        f2.write(bigch)
        f2.write("\n")
        
        
    f2.close()
    f.close()





  
















RemplireMat("FLASH")

    




