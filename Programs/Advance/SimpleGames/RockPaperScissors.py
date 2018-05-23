import random as rm

def main():
  c = 0
  u = 0
  for z in range(3):
    print ("\n\t\t\t===========\n\t\t\trock - paper - scissors")
    comp = rm.choice([1,2,3])
    
    try:
      val = int(input("1.rock \n2.paper \n3.scissors \nYour Choice : "))
    except:
      print ("give valid input ")
      exit()
    
    print ("\n")
    if((val == 3) and (comp == 1)):
      print ("You Lose")
      c = c+1
    elif((comp == 3) and (val == 1)):
      print ("You win")
      u = u + 1
    elif(val == comp):
      print ("Tie")
    elif(val > comp):
      print ("You win")
      u = u + 1
    elif(comp > val):
      print ("You Lose")
      c = c + 1
    else :
      print ("I dont know what had happend !!")
    
    di = {1:"ROCK",2:"PAPER",3:"SCISSORS"}
    
    print ("\n")
    print ("ur choice : ",di[val])
    print ("computer choice : ",di[comp])
  
  print ("\n\t\tFINAL RESULT ")
  if (c > u):
    print ("u lose")
  elif(c < u):
    print ("u win")
  else:
    print ("TIE")
    
if __name__ == "__main__":
    main()
