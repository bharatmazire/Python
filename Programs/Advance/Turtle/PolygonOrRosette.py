import turtle
t = turtle.Pen()
# ask the user for the number of sides or circles, default to 6

number = int(turtle.numinput("number of sides or circle","how many sides or circle in your shape?",6))
# ask the user whether they want a polygon or rosette

shape = turtle.textinput("which shape do you want?","Enter 'p' for polygon or 'r' for rosette:")

for x in range(number):
	if shape == 'r':
		t.circle(100)
	else:
		t.forward(150)
	t.left(360/number)
