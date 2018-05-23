def checkState(state,no_states):
  if (str(state)[:1] == "q" and int(str(state)[1:]) < no_states):
    return True
  print ("wrong input please try again")
  exit()

def checkOp(op):
  if(op < 2 and op > -1):
    return True
  print ("wrong input please try again")
  exit()


def accept_input(no_states,total_list,dicto):

  for i in range(no_states):
    total_list.append([])                                # structure would be like [[q0],[q1],[q2],[q3],....]

    print ("Enter input for state q{}".format(i))

    print ("for q = 0")
    o_state = input("enter state : ")
    if (checkState(o_state,no_states)):
      total_list[i].append(o_state)
    o_op = int(input("enter op : "))
    if(checkOp(o_op)):
      total_list[i].append(o_op)
    dicto.setdefault(o_state,[])
    dicto[o_state].append(o_op)

    print ("for q = 1")
    i_state = input("enter state : ")
    if (checkState(o_state,no_states)):
      total_list[i].append(i_state)
    i_op = int(input("enter op : "))
    if(checkOp(o_op)):
      total_list[i].append(i_op)
    dicto.setdefault(i_state,[])
    dicto[i_state].append(i_op)

  return total_list ,dicto

def generate(total_list,final_list):
  output = {}
  for i in final_list:
      output.setdefault(i,[])
      output[i].append(total_list[int(str(i)[1:2])][0])
      output[i].append(total_list[int(str(i)[1:2])][2])
      output[i].append(final_list[i])
  print (output)
  print ("state:   state     op")
  for i in output:
      print ("{}    {}".format(i,output[i]))
  


def main():
  dicto = {}                                                    # assigining blank dictonary
  total_list = []                                               # assigining blank list
  
  no_states = int(input("please entre number of states : "))    # accept number of states as input
  print ("number of states are : ",no_states)
  
  total_list , dicto = accept_input(no_states,total_list,dicto) # calling function accept input
  
  print ("\nMealy form is: ")
  print("q0 = 0\t q1 = 1")
  print ("\nstate,op, state,op")
  for i in (total_list):
      print (i)
  print("\ndictonary is : ",dicto)
  
  final_list = {}
  for i in dicto:
    if(len(dicto[i]) ==1):
      final_list[i] = dicto[i][0]
    elif (dicto[i][0] == dicto[i][1]):
      final_list[i] = dicto[i][0]
    else:
      final_list[i+str(0)] = 0
      final_list[i+str(1)] = 1

  print ("\n final list for representation of moore is : ",final_list)

  generate(total_list,final_list)

main()
