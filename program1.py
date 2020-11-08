m_awal = 100000000

for i in range(1, 9):
    if(i >= 1 and i <= 2):
        a = m_awal * 0
        print("laba bulan ke-",i,"sebesar",a)
    elif(i >= 3 and i <= 4):
        b = m_awal * 0.01
        print("laba bulan ke-",i,"sebesar",b)
    elif(i >= 5 and i <= 7):
        c = m_awal * 0.05
        print("laba bulan ke-",i,"sebesar",c)
    elif(i == 8):
        d = m_awal * 0.03
        print("laba bulan ke-",i,"sebesar",d)
total = a + a + b + b + c + c + c + d
print("total laba adalah :", total)
