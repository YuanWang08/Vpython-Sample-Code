from vpython import *

ball = sphere(pos=vector(0, 0, 0),
              radius=0.1,
              color=color.blue,
              v=vector(0, 0, 0),
              a=vector(5.0, 0, 0))

dt = 0.001
t = 0.0

gd1 = graph(title='x-t', width=600, height=400, xtitle='t', ytitle='x')
f1 = gcurve(color=color.blue)

gd2 = graph(title='v-t', width=600, height=400, xtitle='t', ytitle='v')
f2 = gcurve(color=color.green)

gd3 = graph(title='a-t', width=600, height=400, xtitle='t', ytitle='a')
f3 = gcurve(color=color.red)

while t < 6:
    rate(1 / dt)
    t = t + dt
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    f1.plot(pos=(t, ball.pos.x))
    f2.plot(pos=(t, ball.v.x))
    f3.plot(pos=(t, ball.a.x))

    if t < 2 and t + dt > 2:
        ball.a.x = -5.0
    if t < 4 and t + dt > 4:
        print('最遠處', t, ball.pos.x, ball.v)
