import turtle
import math
house = turtle.Turtle()


def body(t):
    for i in range(4):
        t.fd(200)
        t.lt(90)

def roof(t):
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(40)
    t.rt(150)
    t.fd(160)
    t.rt(60)
    t.fd(160)
    t.rt(150)
    t.fd(37)

def door(t):
    t.lt(90)
    t.fd(200)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(90)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(90)

def doorknob(t, n, length):
    t.lt(90)
    t.fd(45)
    t.lt(90)
    t.pu()
    t.fd(35)
    t.pd()

    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def window(t, length):
    t.pu()
    t.fd(85)
    t.lt(90)
    t.fd(75)
    t.pd()

    for i in range(4):
        t.fd(length)
        t.lt(90)

    t.fd(20)
    t.lt(90)
    t.fd(40)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.fd(40)

    t.pu()
    t.fd(100)





body(house)
roof(house)
door(house)
doorknob(house, 9, 2)
window(house, 40)

turtle.mainloop()
