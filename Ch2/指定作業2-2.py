from vpython import *

g = 9.8
size = 0.5
m = 1.0
Fg = vector(0, -m * g, 0)
theta = 3 * pi / 180
v0 = 10

gd1 = graph(title="theta-R plot",
            width=600,
            height=400,
            xtitle="theta",
            ytitle="R")
f1 = gcurve(color=color.blue)

gd2 = graph(title="theta-t plot",
            width=600,
            height=400,
            xtitle="theta",
            ytitle="t")
f2 = gcurve(color=color.red)

scene = canvas(width=600, height=600, x=0, y=0, center=vector(0, 0, 0))
floor = box(color=color.green, height=0.01, width=30, length=50)
ball = sphere(color=color.yellow,
              radius=size,
              make_trail=True,
              trail_type="points",
              interval=1)

ball.pos = vector(0, size, 0)
ball.v = vector(v0 * cos(theta), v0 * sin(theta), 0)
dt = 0.001
t = 0.0
show_angle = label(pos=vector(0, -7, 0),
                   box=False,
                   height=20,
                   color=color.yellow)
while True:
    show_angle.text = 'theta = %1.0f deg' % (theta / pi * 180)
    rate(1 / dt)  #ball
    t = t + dt
    ball.a = (Fg) / m
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    if ball.pos.y <= size and ball.v.y < 0:
        f1.plot(pos=(theta, ball.pos.x))
        f2.plot(pos=(theta, t))
        print("T=", t, "R=", ball.pos.x, "theta=", theta / pi * 180)
        theta = theta + 3 * pi / 180
        ball.pos = vector(0, size, 0)
        ball.v = vector(v0 * cos(theta), v0 * sin(theta), 0)
        t = 0
