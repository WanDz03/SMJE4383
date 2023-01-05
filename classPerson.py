from person import Person

if __name__ == '__main__':
	bob = Person('Bob Smith', 42, 30000, 'software')
	sue = Person('Sue Jones', 45, 40000, 'hardware')
	print(bob.name, sue.pay)
	
	print(bob.lastName())
	sue.giveRaise(.10)
	print(sue.pay)
