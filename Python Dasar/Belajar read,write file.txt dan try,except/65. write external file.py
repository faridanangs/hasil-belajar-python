# menulis dan membuat file baru 

###  menggunakan write
# dia akan membuat file baru jika blum ada
# dan menimpa text file jika ada
with open('textfile1.txt','w',encoding='utf-8') as file:
	file.write('Hallo dunia\n')
	file.write('Mari belajat python')
	

### menggunakan append untuk menambah data
# dia akan menambah data bukan menimpa data
# jika kita (print / jalankan) dia akan terus bertambah
###(LEBIH BAIK KITA MENGGUNAKAN WRITE DI ATASNYA SUPAYA DIA TDK TERUS BERTAMBAH)
with open('textfile2.txt','w',encoding='utf-8') as file:
	file.write('Hallo dunia\n')
with open('textfile2.txt','a',encoding='utf-8') as file:
	file.write('Mari belajat python\n')
	file.write('Mari belajat python\n')
	file.write('Mari belajat python\n')
	
### use r+ for write,and read data if data not found maka program akan error jadi file.txt harus di buat dulu baru r+ bisa di gunakan
with open('textfile3.txt','w',encoding='utf-8') as file:
	pass
	
with open('textfile3.txt','r+',encoding='utf-8') as file:
	file.write('Data ke-1\n')
	file.write('Data ke-2\n')
	file.write('Data ke-3\n')
with open('textfile3.txt','r+',encoding='utf-8') as file:
	file.write('Data ke-5\n') #akan mnimpa dta yg paling atas
	file.write('Data ke-6\n')

# ini akan menimpa data yang sudah ada dgan yang baru
with open('textfile3.txt','r+',encoding='utf-8') as file:
	file.write('farid anang samudra ganteng ya nggak')
		
# jika ingin membaca file usahan buat r+ yang baru
with open('textfile1.txt','r+',encoding='utf-8') as file:
	data = file.read()
	print(data)
with open('textfile2.txt','r+',encoding='utf-8') as file:
	data = file.read()
	print(data)
with open('textfile3.txt','r+',encoding='utf-8') as file:
	data = file.read()
	print(data)

'''
INI AKAN ERROR KARNA ok.txt TIDAK BERADA DI FOLDER YG SAMA

with open('ok.txt','r+',encoding='utf-8') as file:
	data = file.read()
	print(data)

JIKA INGIN MEMBACA SEBUAH FILE.TXT USAHAKAN BEDARA DI POLDER YANG SAMA
'''