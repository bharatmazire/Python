#!/usr/bin/python

# WAP to perform various action on dates

class Date_operation():
	def __init__(self):
		self.day   = 00
		self.month = 00
		self.year  = 0000

	def set(self,dd,mm,yy):
		#dd = eval(input("enter date : "))
		#mm = eval(input("enter month : "))
		#yy = eval(input("enter year : "))
		if dd <= 31 and dd > 0 and mm <= 12 and mm > 0 and yy > 0 :
			self.day   = dd
			self.month = mm
			self.year  = yy
			d = str(dd)
			m = str(mm)
			y = str(yy)
			self.date  = d+m+y
		#print ("{}/{}/{}".format(self.day,self.month,self.year)) 

	def get_day(self):
		#print("date is ",self.date)
		return self.day
	def get_month(self):
		#print("month is ",self.month)
		return self.month
	def get_year(self):
		#print("year is ",self.year)
		return self.year
	
	def get(self):
		print ("{}/{}/{}".format(self.day,self.month,self.year))
		return self.day ,self.month ,self.year 		

	def cheack_leap(self):
		if self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0 :
			#print ("{} is leap year ".format(self.year))
			return True
		else:
			#print ("{} is not leap year ".format(self.year))
			return False

	def alpha_neumeric(self,i):
		if eval(i) == 0:
			return " ZERO "
		elif eval(i) == 1:
			return " ONE "
		elif eval(i) == 2:
			return " TWO "
		elif eval(i) == 3:
			return " THREE "
		elif eval(i) == 4:
			return " FOUR "
		elif eval(i) == 5:
			return " FIVE "
		elif eval(i) == 6:
			return " SIX "
		elif eval(i) == 7:
			return " SEVEN "
		elif eval(i) == 8:
			return " EIGHT "
		elif eval(i) == 9:
			return " NINE "
		else:
			return "/"

	def return_in_alpha(self):
		for i in self.date:
			date = self.alpha_neumeric(i)
			print(date,end = '')



if __name__ == '__main__':
	obj1 = Date_operation()

	dd = eval(input("enter date : "))
	mm = eval(input("enter month : "))
	yy = eval(input("enter year : "))
	obj1.set(dd,mm,yy)

	print (obj1.get_day())
	print (obj1.get_month())
	print (obj1.get_year())
	dd,mm,yy = obj1.get()
	print ("{}/{}/{}".format(dd,mm,yy))

	if obj1.cheack_leap():
		print("Its leap year !!!")
	else:
		print("Its not leap year !!!")

	obj1.return_in_alpha()