import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# Ask the user for the number of circles in their rosette, default to 6

number_of_circles = int(turtle.numinput("Number of Circles","How many circles in your rosette?",6))
colors = ["red","white","purple"]

for x in range(number_of_circles):
	t.pencolor(colors[x%3])
	t.circle(100)
	t.left(360/number_of_circles)
