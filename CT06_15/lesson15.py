print("Hello from lesson 15")
import turtle

window = turtle.Screen()
window.setup(width=600, height=600)

artist = turtle.Turtle()
artist.shape("turtle")
artist.color("orange")
artist.fillcolor("green")
# artist.forward(200)

# turtle.seth(90)
# # artist.left(90)
# # artist.right(100)

# # for count in range(5):
# #     artist.forward(150)
# #     artist.left(72)

# # artist.circle(150)
# artist.up()
# artist.goto(-300, 0)
# artist.down()
# artist.setx(300)
# artist.back(300)

import random
artist.up()

alist = ["purple", "navy blue", "orange", "red", "green", "teal", "yellow"]
for count in range(1000000):
    newx = random.randint(-280, 280)
    newy = random.randint(-280, 280)


    value = random.choice(alist)
    artist.color(value)
    artist.seth(random.randint(0, 360))
    artist.goto(newx, newy)
    artist.stamp()

window.mainloop()