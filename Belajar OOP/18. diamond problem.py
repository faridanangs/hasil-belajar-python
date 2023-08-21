#Diamon problem


"""
CARA JALANNYA SEPERTI INI

			 	(4) A
	
(2) B							 (3) C


			 	(1) D

"""
class A:
	def show(self):
		print('Ini adalah show A')
	
class B(A):
	def show(self):
		print('Ini adalah show B')

class C(A):
	def show(self):
		print('Ini adalah show C')

class D(B,C):
	pass

objek = D()
objek.show()

help(objek)