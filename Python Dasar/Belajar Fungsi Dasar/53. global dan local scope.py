# global dan local scope

# => local scope hanya dapat di jalankan di fungsi tersebut tdk bisa di jalankan di luar fungsi


# contoh sederhana local scope
def fungsi():
	nama = 'farid','anang','samudra',175,158
	print(nama)
#	return nama 

fungsi()
# print(nama)  |=>  ini akan error karna nama hanya untuk local bukan untuk global. walaupun sudah di return dia akan tetap error

# contoh sederhana global scope dan mengubah nilai global scope
angka = 2
def ubah_angka(nilai_baru):
	global angka#global use  for change nilai global scope
	angka = nilai_baru
print(angka)
ubah_angka(10)
print(angka)

"""
global hanya di gunakan di fungsi untuk mengubah nilai global scope jika di for,if,while maka global scope dapat di ubah tanpa menggunakan kata global di depan angka yg mau di ubaj
"""