import turtle as trt
import time
def star_shape():
    scn = trt.Screen()
    pos = trt.Turtle()
    scn.title("Star-Shape")
    scn.setup(420,320)
    scn.bgcolor('black')
    clrs = ['green','yellow','red','blue','purple']
    pos.pensize(4)
    pos.penup()
    pos.setpos(-90,30)
    pos.pendown()
    for i in range(5):
        pos.pencolor(clrs[i])
        pos.forward(200)
        pos.right(144)
    time.sleep(0.75)
    pos.penup()
    pos.setpos(0,-140)
    pos.pendown()
    pos.pencolor('white')
    pos.write("Almasi.Digital", font=("Back to 1982", 12,'normal'))
    pos.ht()
    time.sleep(2.5)
    trt.bye()
star_shape()
