##looping pada list



### List comperension
# campur
data = ['farid',10,14,]
[print(f'data = {i}')for i in data]
print('')
# pangkat
data_angka = [10,78,54,10]
data_pangkat = [i**3 for i in data_angka]
print(data_pangkat)
print('')


### enumerate
data = ['farid','ucok','usdima']
for x,y in enumerate(data):
	print(f'index = {x}, nama = {y}')