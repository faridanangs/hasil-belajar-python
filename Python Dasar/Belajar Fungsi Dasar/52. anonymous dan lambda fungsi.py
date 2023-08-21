# lambda pada fungsi


#pangkat pake lambda
pangkat = lambda x,y:x**y
print(pangkat(2,2))
print('')

# sort pake lambda dan mengurutkan sesuai nama terkecil
data_list = ['anangs','diana','udin']
data_list.sort(key = lambda x:len(x))
print(data_list)
print('')

#sort pake fungsi dan mengurutkan sesuai yg terkecil
data_list = ['anangs','diana','udmn','usman','ucup']
def sort(data):
	return len(data)
data_list.sort(key=sort)
print(data_list)
print('')


#data list angka pake filter lambda
angka = [1,2,3,4,5,6,7,8,7,5,8,5,3,2,5,7,8,9,9,9]
angka_lambda = list(filter(lambda x:x<5,angka))
print(angka_lambda)
print('')
# angka list genap
angka_genap = list(filter(lambda x:x%2 == 0,angka))
angka_genap.sort()
print(angka_genap)
print('')
# angka list ganjil
angka_ganjil = list(filter(lambda x:(x%2 !=0),angka))
angka_ganjil.sort()
print(angka_ganjil)
print('')
#angka list kelipatan 3
angka_pangkat = list(filter(lambda x:(x%3 == 0),angka))
angka_pangkat.sort()
print(angka_pangkat)