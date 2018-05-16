#
#	remaining part : use threads to run each function
#			 so it will generate each letter seperatly
#

import turtle
import time
#import thread as thrd

def i():
	t0 = turtle.Pen()
	t0.pencolor('black')
	t0.width(2)
	t0.left(90)
	t0.forward(90)
	t0.left(90)
	t0.forward(230)
	t0.pencolor('blue')
	t0.left(90)
	t0.forward(100)

def heart():
	t1 = turtle.Pen()
	t2 = turtle.Pen()
#	turtle.bgcolor('black')
	t1.pencolor('red')
	t2.pencolor('red')
	t1.width(1)
	t2.width(1)
	t1.left(90)
	t2.left(90)
	for i in range(230):
		t1.forward(1)
		t1.left(1)
		t2.forward(1)
		t2.right(1)
	for i in range(135):
		t1.forward(1)
		t2.forward(1)
def u():
	t3 = turtle.Pen()
	t4 = turtle.Pen()
	t3.pencolor('black')
	t4.pencolor('black')
	t3.forward(230)
	t4.forward(230)
	t3.pencolor('yellow')
	t4.pencolor('yellow')
	t3.width(2)
	t4.width(2)
	t3.left(180)
	for i in range(90):
		t3.forward(1)
		t3.right(1)
		t4.forward(1)
		t4.left(1)
	t3.forward(90)
	t4.forward(90)

def main():
	turtle.bgcolor('black')
#	thrd.start_new_thread(i)
#	thrd.start_new_thread(heart)
#	thrd.start_new_thread(u)
#	t1.start()
#	t2.start()
#	t3.start()

#	t1.join()
#	t2.join()
#	t3.join()
	
	# draw I
	i()
	# draw HEART <3
	heart()
	# draw U
	u()
	# sleep for while
	time.sleep(3)

if __name__ == '__main__':
	main()
#	t1 = thrd.Thread(target=i)
#	t2 = thrd.Thread(target=heart)
#	t3 = thrd.Thread(target=u)

#	t1.start()
#	t2.start()
#	t3.start()

#	t1.join()
#	t2.join()
#	t3.join()
