import turtle

spiral = turtle.Turtle()
spiral.shape("turtle")
spiral.speed("normal") # slow, fast

for i in range(60):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()
