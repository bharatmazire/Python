import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","purple","white","brown","gray","pink"]
family = [] 					# set up an empty list for family names

# ask for the first name

name = turtle.textinput("my family","Enter name, or just [ENTER] to end :")

# keep asking for names

while name != "":
	family.append(name)
	name = turtle.textinput("my family","Enter name, or just hit [ENTER} to end :")

# draw a spiral of the name on the screen

for x in range(100):
	t.pencolor(colors[x%len(family)])	# roatate through the colors
	t.penup()				# don't draw the regural spiral lines
	t.forward(x*4)				# just move the turtle on the screen
	t.pendown()				# draw the next family member's name
	t.write(family[x%len(family)],font = ("Arial",int((x+4)/4), "bold"))
	t.left(360/len(family) + 2)		# turn left for our spiral
