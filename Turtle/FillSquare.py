import turtle

turtle.color('brown')

turtle.begin_fill()
counter = 0
while counter < 4:
  turtle.forward(100)
  turtle.left(90)
  counter = counter + 1

turtle.end_fill()
