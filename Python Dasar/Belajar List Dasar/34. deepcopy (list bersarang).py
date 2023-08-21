### deepcopy
from copy import deepcopy



### List bersarang
data_1 = [1,8,9]
data_2 = [7,2,5]
data_2D = [data_1,data_2]
print(data_2D)
print('\n\n')


## melihat data yang ada di dalam list    
# kalimat = data_2D[index list][index dalam list]
lihat_data = data_2D[1][1]
print('List di dalam [0][1] =',lihat_data)
print('\n\n')


# (  SEKARANG KITA BEBAS MERUBAH DATA LIST SETELAH DI deepcopy(data_list)    )


### Mengkopi Semua data list di dalam baik di luar use
## deepcopy(data_list)
data_deepcopy = deepcopy(data_2D)
print('List setelah di deepcopy: ',data_deepcopy)
print('\n\n')

# <data list>
print('Data 2D\t     :',data_2D)
print('Data_deepcopy:',data_deepcopy)
print('\n')

print(f'Id data_2D\t: {hex(id(data_2D))}')
print(f'Id data_deepcopy: {hex(id(data_deepcopy))}')
# </data list>
print('')

### sekarang cobak kita rubah
data_deepcopy[0][2] = 2293

# data_2D tdk ikut berubah karna sudah di deepcopy()
print('Data 2D\t     :',data_2D)
print('Data_deepcopy:',data_deepcopy)
