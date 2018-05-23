import turtle

turtle.color('brown')       # setting color to brown

turtle.begin_fill()         # start filling color

for i in range(4):          # settign loop
  turtle.forward(100)       # forwarding with distance 100
  turtle.left(90)           # moving head to left 90 degree
  
turtle.end_fill()           # filling color stop
