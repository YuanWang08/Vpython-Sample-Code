from vpython import *

g = 9.8
size = 2.0
height = 15.0
m = 1.0
Fg = vector(0, -m * g, 0)

floor = box(color=color.yellow, height=0.1, width=30, length=50)

ball = sphere(color=color.yellow,
              radius=size,
              make_trail=True,
              trail_type="points",
              interval=100)

ball2 = sphere(color=color.red,
               radius=size,
               make_trail=True,
               trail_type="points",
               interval=100)

ball3 = sphere(color=color.green,
               radius=size,
               make_trail=True,
               trail_type="points",
               interval=2)

ball.pos = vector(0, 0, 0)
ball.v = vector(10, 10, 0)

ball2.pos = vector(0, 0, 0)
ball2.v = vector(10, 10, 0)

ball3.pos = vector(0, size, 0)
ball3.v = vector(10, 10, 0)

dt = 0.001
t = 0
damp = 0.4
k = 0.4
while True:
    rate(1 / dt)  #ball
    t = t + dt

    ball.a = Fg / m
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    if ball.pos.y <= 0:
        ball.pos.y = 0
    #ball2
    ball2.a = (-damp * ball2.v + Fg) / m
    ball2.v = ball2.v + ball2.a * dt
    ball2.pos = ball2.pos + ball2.v * dt
    if ball.pos.y <= 0:
        ball2.pos.y = 0
        break
t = 0
dt = 0.001
while True:
    rate(1 / dt)
    t = t + dt
    ball3.pos.x = ball.v.x * (1 - exp(-k * t)) / k
    ball3.pos.y = -g * t / k + (k * ball3.v.y + g) * (1 - exp(-k * t)) / k**2
    ball3.pos.z = 0
    if ball3.pos.y < 0:
        break
