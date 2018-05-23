def checkState(val , no_state):
  if(val[:1] == "q" and val[1:] <= no_state):
    return True
  print ("Bad input")
  exit()

def checkop(val):
  if(val == 1 or val == 0):
    return True
  print ("Bad input")
  exit()

def accept(no_state):
  dicto = {}
  listo = []
  for i in range(no_state):
    listo.append([])
    print("Enter values for state q{}".format(i))
    name = "q"+str(i)
    #listo[i].append(name)
    state_1 = input("Enter state 1 : ")
    if (checkState(state_1,no_state)):
      listo[i].append(state_1)
    state_2 = input("Enter state 2 : ")
    if (checkState(state_2,no_state)):
      listo[i].append(state_2)
    output = int(input("output : "))
    #listo[i].append(output)
    if (checkop(output)):
      dicto[name] = output
  return listo , dicto 
  
def show_op(no_state,listo,dicto):
  print ("st st1 op1 st2 op2 ")
  for i in range(no_state):
    print ("q{}".format(i),end="")
    for j in listo[i]:
      print(" ",j,end="")
      print(" ",dicto[j],end="")
    print ("")
    
def main():
  no_state = int(input("Enter total number of states : "))
  listo , dicto = accept(no_state)
  print (listo , dicto)
  print ("output in melay form ")
  show_op(no_state,listo,dicto)
  
main()
