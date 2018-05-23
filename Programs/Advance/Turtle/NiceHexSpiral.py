import turtle					# importing turtle library

colors = ['red' , 'purple' , 'blue' , 'green' , 'yellow' , 'orange']	# listing out colors for further use

t = turtle.Pen()				# initializing Pen
turtle.bgcolor('black')				# setting background color to black
for x in range(360):				# setting loop for value 360
	t.pencolor(colors[ x % 6 ])		# selecting pen color from previously defined list (changing color per iterations)
	t.width(x/100 + 1)			# setting width (chaning per iteration)
	t.forward(x)				# drawing 'x' amount (chaning per iteration)
	t.left(59)				# rotating pointer to left by 59 degrees
