import turtle

for i in range(2,7):								# for loop for setting sides range (from 2 to 6)
	t = turtle.Pen()							# setting pen
	turtle.bgcolor("black")							# setting background color to black
	sides = i								# getting sides from loop value
	colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']		# colors list
	for x in range(50):							# loop
		t.pencolor(colors[x%sides])					# selecting color for pen from list
		t.forward(x * 3/sides + x)					# forwarding pen with some distance
		t.left(360/sides +1)						# moving pen head to some distnce
		t.width(x*sides/200)						# setting pen width (increasing according to loop)
	t.clear()								# clearing whatever we have drew so next shape will come here
