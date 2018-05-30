import turtle as t

def showTurtle():
    t.st()
    return

def getPos(x,y):
    print("(", x, "," ,y,")")
    return

def hideTurtle(x,y):
    t.ht()
    return

def main():
    t.speed(20)
    t.shapesize(1000,1000)
    t.up()
    t.goto(1000,0)
    t.ht()
    t.onkey(showTurtle,"a")
    t.listen()
    t.onclick(getPos)
    t.onrelease(hideTurtle)
t.mainloop()
main()
