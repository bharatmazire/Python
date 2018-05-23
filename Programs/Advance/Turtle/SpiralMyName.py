import turtle

t = turtle.Pen()							# initialize pen
turtle.bgcolor("black")							# set background color to black
colors = ["red", "yellow", "blue", "green"]				# setting color list

your_name = turtle.textinput("Enter Your name", "What is your name?")	# ask your for entering name. Through text field 

for x in range(100):							# loop
	t.pencolor(colors[x%4])						# pen color from list
	t.penup()							# pen up to print nothing
	t.forward(x*4)							# moving pen to x*4 dist.
	t.pendown()							# putting pen down
	t.write(your_name, font = ("Arial",int((x+4)/4),"bold"))	# printing name
	t.left(92)							# moving pen head to 92 degree
