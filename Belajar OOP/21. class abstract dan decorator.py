###class abstract dan decorator

from abc import ABC,abstractmethod


class Button(ABC):
	def __init__(self,set_link):
		self.link = set_link
	
	@abstractmethod
	def click(self):
		pass
		
	@property
	@abstractmethod
	def link(self):
		pass
		
class Pushbutton(Button):
	def click(self):
		print('Go to: {} '.format(self.link))
		
# jika kita ingin mengakses/mngubah abstract link kita harus inheritance super class tempat abstrack di simpan
	@Button.link.setter
	def link(self,input):
		self.__link = input
		
	@link.getter
	def link(self):
		return self.__link
		
	
	
tombol1 = Pushbutton('falovedi.epizy.com')
tombol1.click()
