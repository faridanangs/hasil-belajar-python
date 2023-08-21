## PROGRAM UTAMA

from module.package.matematika import tambah,kali,pangkat
from module.fisika import kecepatan

### matematika
#Tambah
tambah = tambah(10,8,5,8,9)
print(f'Hasil tambah = {tambah}')
#Kali
kali = kali(19,8,8,0)
print(f'Hasil kali = {kali}')
#Pangkat
pangkat = pangkat(3)(2)
print(f'Hasil pangkat = {pangkat}')

### fisika
kecepatan = kecepatan(6,5)
print(kecepatan)