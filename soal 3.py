batas_atas = 24
batas_bawah = 10
print("Bilangan prima antara",batas_bawah,"and",batas_atas)
for angka in range(batas_bawah,batas_atas + 1):
    if angka > 1:
        for i in range(2,angka):
            if (angka % i) == 0:
                print(angka,'ini bukan prima')
                break
        else:
            print(angka, 'ini prima')
