import turtle
import tkinter


class MyTurtle(turtle.Turtle):
    def forward(self, n):
        self.backward(n)

t1 = turtle.Turtle()
t1.shape('turtle')
t1.forward(100)

t2 = MyTurtle()
t2.forward(150)

turtle.done()