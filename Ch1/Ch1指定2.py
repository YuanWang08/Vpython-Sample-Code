from vpython import *

x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.green)
y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.red)
z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue)

ball = sphere(pos=vector(0, 0, 0),
              radius=0.1,
              color=color.yellow,
              v=vector(3.0, 0, 0),
              a=vector(-1.0, -0.5, 0))

t = 0
dt = 0.001
tplot = 0

while t < 6:
    rate(1 / dt)
    t = t + dt
    tplot = tplot + dt
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt

    if tplot < 0.4 and tplot + dt >= 0.4:
        arrow(color=color.green, pos=ball.pos, axis=ball.v,
              shaftwidth=0.05)  #畫速度箭頭
        arrow(color=color.red, pos=ball.pos, axis=ball.a,
              shaftwidth=0.05)  #畫加速度箭頭
        sphere(color=color.yellow, pos=ball.pos, radius=0.1)
        tplot = 0

    if ball.v.x > 0 and ball.v.x + ball.a.x * dt < 0:
        print('當X座標極大值時', '速度', ball.v, '位置', ball.pos, '出發時間', t)
