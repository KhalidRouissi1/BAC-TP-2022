


def maxn(n):
    a_list = [int(x) for x in str(n)]

    for i in range(0,len(a_list)-1):
        max=i
        for j in range(i+1,len(a_list)):
   
            if(a_list[max]>a_list[i]):
                max = j
                
            if(max != i):
                aux=a_list[i]
                a_list[i]=a_list[max]
                a_list[max] = aux

maxn(88955)

a_list = [int(x) for x in str(88955)]
a_list.sort(reverse=True)
# print(a_list)

prime_numbers = [11, 3, 7, 5, 2]





l = [1, 2, 3]

s = [str(integer) for integer in l]
a_string = "".join(l)

res = int(a_string)
print(res)
