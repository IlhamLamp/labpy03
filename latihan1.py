import random
n = int(input("Masukkan jumlah n: "))

for i in range(1, n+1):
    while(True):
        n = random.random()
        if(n<0.5):
            break
    print("Data ke:",i,"=>",n)
