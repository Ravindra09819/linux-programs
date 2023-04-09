class Bookstore:
    NoofBooks=0

	def __init__(self,name,author):
		Bookstore.NoofBooks+=1
		self.name=name
		self.author=author

	def display(self):
		print("No of Books :- ",self.NoofBooks)
		print("Name of author :- ",self.author)
		print("Book Name :-",self.name)

obj1=Bookstore("Linux system Programming","Robert Love")
obj1.display()

obj2=Bookstore("Programming in c","Dennis Ritchie")
obj2.display()