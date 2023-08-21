### Copy pada data list


data_a = ['usep','udeng','usmang']

# menyalin data adres yg sama
data_b = data_a
print(data_a)
print(data_b)
print('')

# mengubah salah satu data
# tapi dua" nya berubah di krnakan adres yg sama
data_b[2] = 'gegola'
print(data_a)
print(data_b)
print('')

# setelah di copy()
data_c = data_a.copy()
print(data_a)
print(data_b)
print(data_c)
print('')

# setelah di ubah
# data_a dan data_b  tdk ikut brubah di karnakan adresnya berbeda dengan data_c di karnakan sudah di copy()
data_c[2] = 'FGHsHs'
print(data_a)
print(data_b)
print(data_c)