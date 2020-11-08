max = 0

while(True):
    bil = int(input("Masukkan bilangan: "))
    if(max < bil):
        max = bil
    elif(bil == 0):
        break

print("Bilangan terbesar adalah: ",max)
