

def sasirN():
    n=int(input("Donner moi n "))
    while(n>9999 or n <1000):
        n=int(input("Donner moi n "))
    return n 


# def min(n):
#     a_list = [int(x) for x in str(n)]

#     for i in range(1,len(a_list)-1):
#         min=i
#         for j in range(i+1,len(a_list)):
#             if(a_list[min]<a_list[i]):
#                 min = j
#             if(min!=i):
#                 aux=a_list[i]
#                 a_list[i]=a_list[min]
#                 a_list[min] = aux
#     print(a_list)

 



f=open("suite.txt",'w')
def remplire(n):
    aux=0
    liste =[int(x) for x in str(n)]
    diff =liste.sort(reverse=True)-liste.sort()
    while(aux != diff):
        f.write(str(diff))
        aux = diff
        a_liste = [int(x) for x in str(aux)]
        s = [str(integer) for integer in a_liste.sort(reverse=True)]
        
        u= "".join(s)
        s2=[str(inger) for inger in a_liste.sort()]
        uu = "".join(s2)
        
        diff = u-uu
    f.close()
    print(diff)
n=sasirN()
remplire(n)