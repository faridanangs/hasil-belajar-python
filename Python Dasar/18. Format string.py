### ###    Format String

## angka
angka = 26182.3
print(f'Angka = {angka}')
print('')

## bilangan bulat
angka = 10
print(f'Bilangan bulat = {angka:d}')
print('')

## bilangan ordo ribuan
angka = 10000000
print(f'Bilangan ribuan = {angka:,}')
print('')

## bilangan decimal
angka = 100.20201
print(f'Bilangan decimal = {angka:.2f}')
print('')

## menampilkan leading zero
angka = 100.20201
print(f'Lht leading zero = {angka:08.2f}')
print('')

## mengoprasikan persentase %
angka = 0.048
print(f'Persen dari {angka} = {angka:.2%}')
print('')

### oprasi angka lain (binary, hexadecimal, octal, )
angka = 1212
print(f'Nilai binary dari {angka} = {bin(angka)}')
print(f'Nilai octal dari  {angka} = {oct(angka)}')
print(f'Nilai hexa dari   {angka} = {hex(angka)}')