from vpython import *

size = 0.1  #球的大小
theta = 0.0  #初始角度
R = 1.0  #圓周運動半徑
omega = 2 * pi  #角速度大小=單位時間繞過的角度
t = 0.0  #初始時間

scene = canvas(width=500,
               height=500,
               center=vector(0, 0, 0),
               background=vector(148.0 / 225, 228.0 / 225, 204.0 / 225))

ball = sphere(radius=size,
              color=color.blue,
              make_trail=True,
              interval=1,
              retain=900)

ball.pos = vector(R, 0, 0)  #球的初始位置
t = 0.0  #初始時間
dt = 0.001  #時間間隔

pre_theta = theta
back = False

N = 20

while True:
    rate(1 / dt)
    pre_pre_theta = pre_theta  #前前時刻的角度
    pre_theta = theta  #前一時刻的角度
    theta += omega * dt  #t時刻的角度
    ball.pos = vector(R * cos(theta), R * sin(theta), 0)
    t += dt  #計時器
    if back:
        plot_t = t % (period_t / N)  #將週期切成N等分，並用餘數除法設定畫圖時間點
        if plot_t + dt >= period_t / N and plot_t < period_t / N:  #畫圖時間判斷點
            cylinder(radius=size / 50,
                     color=color.black,
                     pos=vector(0, 0, 0),
                     axis=vector(ball.pos.x, ball.pos.y, 0))  #畫細線
    if pre_theta % (2 * pi) > pre_pre_theta % (2 * pi) and pre_theta % (
            2 * pi) > theta % (2 * pi):
        print('period = ', t)
        back = True  #如果跨過原點代表back這個事件發生了，所以把False改成True
        period_t = t  #用一個新的變數period_t把週期存下來
        t = 0
