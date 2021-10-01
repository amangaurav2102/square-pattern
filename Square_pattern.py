import turtle
t = turtle.Turtle()

s = turtle.Screen()
c = 0
while 1:
	for i in range(4):
		t.forward(250)
		t.right(90)
	t.right(3)
	c += 1
	if c>= 360/3:
		continue

turtle.done()


