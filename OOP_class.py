class Account: # супер класс "Счет"
	amount = 0
	
class CreditCard(Account): # подкласс "Кредитная карта", который наследует атрибут (параметр) "Сумма"
	def add(self, n): # метод ADD, self - ссылка на экземпляр класса
		self.amount += n
		return self.amount
		
	def withdraw(self, n): # метод WITHDRAW, self - ссылка на экземпляр класса
		self.amount -= n
		return self.amount
		
Petrov = CreditCard() # экземпляр класса "CreditCard" Петров
Ivanov = CreditCard() # экземпляр класса "CreditCard" Иванов

print('Funds on the Petrov credit card is ', Petrov.amount)
print('Adding to Petrov`s account ', Petrov.add(110))
print('After adding sum, funds on the Petrov credit card is ', Petrov.amount)
print('Withdraw from Petrov`s account ', Petrov.withdraw(67.56))
print('After withdraw sum, funds on the Petrov credit card is ', Petrov.amount)
print('Funds on the Ivanov credit card is ', Ivanov.amount)
print('Adding to Ivanov`s account ', Ivanov.add(329))
print('After adding sum, funds on the Ivanov credit card is ', Ivanov.amount)
print('Withdraw from Ivanov`s account ', Ivanov.withdraw(67.56))
print('After withdraw sum, funds on the Ivanov credit card is ', Ivanov.amount)