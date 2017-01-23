s = input()
def chk(s):
	if s == s[::-1]:
		return s+" is palindrome"
	else:
		return s+" is not palindrome"
print(chk(s))

# i = 0
# j = -1
# while (x[i] == x[j] and i<int(len(x)/2)):
# 	i+=1
# 	j-=1