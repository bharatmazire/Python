import os

print("Linux terminal in python.\nType exit to quite")
comment = ""
while (comment != "exit"):
    comment = raw_input("$ ")
    os.system(comment)
