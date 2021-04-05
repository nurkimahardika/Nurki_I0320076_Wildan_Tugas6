daftar_nilai = input('Ketikkan semua nilai yang akan dirata-rata dan pisahkan dengan tanda koma tiap-tiap nilai!>')
list_nilai = daftar_nilai.split(',')
list_nilai_akhir = [int(x) for x in list_nilai]

total = 0

for nilai in list_nilai_akhir :
    total = total + nilai
nilai_rata = total/len(list_nilai_akhir)

print('jumlah total nilai anda adalah: ', total)
print('Rata-rata keseluruhan nilai yang anda input adalah: ', nilai_rata)