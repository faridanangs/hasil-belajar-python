### list ==> aray, mengakses dengan menggunakan index

data_list = ['ujeng','usmeang','kuseng']
print('index list kuseng = ',data_list.index('kuseng'))
print('Data list index 2 =',data_list[2])
print('\n\n')

### dictionary (dict) asociative array identifer ==> key
# dictionary dapat di panggil key nya saja
''' data_dict = {
	'key':'value'
} '''

### data dict dapat memanggil data list,number,dan juga data dict


dict = {
'ng' : 'anang',
'frd' : 'farid',
'wgs' : 'wagas',
}

data_dict = {
'key' : 'value',

'rti' : 'roti bakar',
'nmbr' : 10121819,
'dtlist' : data_list,
'dict' : dict
}

print(f'''
Data dict key rti: {data_dict["rti"]}

Data dict key nmbr: {data_dict["nmbr"]}

Data dict key dtlist: {data_dict["dtlist"]} 

Data dict key dict: {data_dict["dict"]}
''')