#Consider the bouncing ball example from the looping lecture. We stored an x and y value for a single ball and moved it around the screen. We can now easily draw MANY balls using the same logic. Instead of storing a single x/y pair, we can store a list of x/y pairs.

from SimpleGraphics import *
import random
setAutoUpdate(False)

xs = []
ys = []
dxs = []
dys = []
num_balls = 50000

for i in range(num_balls):
	xs.append(random.randint(100, 700))
	ys.append(random.randint(100, 500))
	dxs.append(random.randint(0,4))
	dys.append(random.randint(0,4))

width = 25
height = 25
total_width = 800
total_height = 600

while True:
	clear()
	for i in range(num_balls): #this is the index values for each of the balls
		xs[i] += dxs[i]
		ys[i] += dys[i]

		if (xs[i] + width >= total_width) or (xs[i] <= 0):
			dxs[i] *= -1

		if (ys[i] <= 0) or (ys[i] + height >= total_height):
			dys[i] *= -1

		ellipse(xs[i], ys[i], width, height)

	update()
