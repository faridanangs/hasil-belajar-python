### alternatip membuat list
data = range(0,20,2) # range(start,stop,step)
data = list(data)
print(data)
print('')

### list menggunakan for loop
list_for = [i for i in range(0,11)]
print(list_for)
print('')

### list menggunakan for if
list_for_if = [i for i in range(0,10) if i != 7]
print(list_for_if)
# for if ganjil
list_genap = [i for i in range(0,16) if i%2 != 0]
print(list_genap)
# for if genap
list_genap = [i for i in range(0,16) if i%2 ==0]
print(list_genap)