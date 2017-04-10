#!/usr/bin/python

# code for booths multiplicatio 

import copy as cp

def AddNum(ans, num):
	c = '0'
	i = 7
	while i >= 0:
		if ans[i] == '0' and num[i] == '0':
			ans[i] = c
			c = '0'
		elif ans[i] == '0' and num[i] == '1':
			if c == '0':
				ans[i] = '1'
			else:
				ans[i] = '0'
				c = '1'
		elif ans[i] == '1' and num[i] == '0':
			if c == '0':
				ans[i] = '1'
			else:
				ans[i] = '0'
				c = '1'
		elif ans[i] == '1' and num[i] == '1':
			if c == '0':
				ans[i] = '0'
				c = '1'
			else:
				ans[i] = '1'
				c = '1'
		i-=1
	return ans

def RightShift(num):
	i = 16
	while i > 0:
		num[i] = num[i-1]
		i-=1
	return num

def BoothMul(num1, num2, num2c):
	#create ans array with num*2 + 1 bits
	ans = ['0' for x in range (8)]
	ans.extend(num1)
	ans.append('0')
	
	i = 0
	while i < 8:
		if ans[15] == '0' and ans[16] == '1':
			ans = AddNum(ans, num2)
		elif ans[15] == '1' and ans[16] == '0':
			ans = AddNum(ans, num2c)
		ans = RightShift(ans)
		i+=1
	ans.pop()
	return ans

def padToEight(num):
	num.reverse()
	pad = 8 - len(num)
	num.extend(['0' for x in range (pad)])
	num.reverse()
	return num

def TwoCompliment(num2):
	num = num2
	num.reverse()
	idx = num.index('1')+1

	while idx<len(num):
		if num[idx] == '0':
			num[idx] = '1'
		else:
			num[idx] = '0'
		idx+=1
	num.reverse()
	return num

def accept():
	no1 = int(input("Enter Number 1 (0< num <127): "))
	no2 = int(input("Enter Number 2 (0< num <127): "))

	no1 = list(bin(no1))[2:]
	no2 = list(bin(no2))[2:]

	no1 = padToEight(no1)
	no2 = padToEight(no2)
	no3 = cp.deepcopy(no2)

	return no1 , no2 , no3

def main():
	no1 , no2 , no3 = accept()

	no2c = TwoCompliment(no3)
	
	ans = BoothMul(no1, no2, no2c) 
	print(int(eval(str(ans).replace(',','')[1:-1]),2))

if __name__ == '__main__':
	main()
