### 1. Oprasi dan manipulasi string

nama = 'farid anang samudra'

### 2. Menghitung jumlah str
print('jumlah karakter',nama,'=',len(nama))

### 3. Melihat alfabert min dan max
#min spasi
print('alfabert paling awal =',min(nama))
# max
print('alfabert paling akhir =',max(nama))

### 4. Menggunakan imdexing
print('Index ke 0 dari',nama,'=',nama[0]) #di mulai dari 0
print('Index ke -1 dari',nama,'=',nama[-1]) #di mulai dari 0
# menyambung index
print('Index ke 0:6 dari',nama,'=',nama[0:6]) #di mulai dari 0

### 5. Ascii code dan char asci
data = ord(' ')
# ascii code
print('Ascii code untuk spasi =',str(data))

data = 102
# char ascii
print('char asci untuk 102 =',chr(data))
