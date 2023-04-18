import pickle


f=open("test.dat","ab")


for i in range(5):
    pickle.dump(i,f)


f.close()
f=open("test.dat","rb")


for i in range(5):
    k=pickle.load(f)

    print(k)
