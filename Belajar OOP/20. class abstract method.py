### ABSTRAK CLASS
##Dimana class harus mengambil method yang ada di super class dgn cara mengimport module yg ada di pythom

from abc import ABC,abstractmethod

class Button(ABC):
	
	@abstractmethod
	def click(self):
		pass
		
class Pushbutton(Button):
	def click(self):
		print('Ini adalah Pushbutton')
		
class Radiobutton(Button):
# method pencet akan error karna dia menginheritance class abstract maka dia juga harus mnggunakan method class abstract tersebut spya tdk error yaitu (click)
		def pencet(self): 
			print('Ini adalah Radiobutton')
		
		
tombol1 = Pushbutton()
tombol2 = Radiobutton()

tombol1.click()
tombol2.pencet()