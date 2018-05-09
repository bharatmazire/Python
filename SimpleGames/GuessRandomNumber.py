import random as rm

def main():
  print ("RANDOM NUMBER GUESS !!")
  
  value = rm.randint(1,100)
  chances = 10
  flag = 0
  
  while chances != 0:
    print ("Remaining Chances !!!!",chances)
    number = int(input("Enter number : "))
    if value == number:
      print ("Well Done...")
      flag = 1
      break
    elif value < number:
      print ("Value Smaller than you enterd!!")
    elif value > number:
      print ("Value Greater than you enterd!!")
    chances = chances - 1
  
  if flag == 0:
    print ("Chances are over !!")
    print ("number is ",value)

main()
