#Write a program that, by clicking on the left mouse button, draws a star in the place of the click.
# The background of the image should be black, while the stars can have different sizes,
# colors and have a different number of sides.


import turtle as t
from random import randint, uniform


def ray(dist, a):
    x0, y0 = t.pos()
    t.fd(dist)
    x1, y1 = t.pos()
    t.bk(dist)
    t.right(90)
    t.fd(a)
    x2, y2 = t.pos()
    t.right(180)
    t.fd(2 * a)
    t.right(90)
    t.begin_fill()
    t.goto(x1, y1)
    t.goto(x2, y2)
    t.end_fill()
    t.goto(x0, y0)


def star(x, y):
    size = uniform(10, 50)
    k = size / randint(3, 7)
    n = randint(3, 15)
    t.color(tuple(randint(0, 255) for _ in 'rgb'))
    t.up()
    t.goto(x, y)
    t.down()
    t.seth(uniform(0, 360 / n))
    t.tracer(3)
    for _ in range(n):
        ray(size, k)
        t.left(360 / n)


def left_mouse_click(x, y):
    star(x, y)


t.Screen().setup(640, 480)
t.Screen().bgcolor('black')
t.ht()
t.speed(0)

t.Screen().onclick(left_mouse_click)
t.Screen().listen()