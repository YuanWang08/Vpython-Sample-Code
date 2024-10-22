"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/25
    特色課程 Lecture 09 List的練習_萬有引力_球與圓環的SHM
    9_01_SHM_Circle and Ball_Fg.py
"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
G=2000  #重力常數
M=1.0     #紅球質量(圓環質量為360*M)
m=1.0     #綠球質量
dt = 0.001          
t = 0
R = 10     #圓環半徑
"""
    2. 畫面設定
"""
scene = canvas(width=1000, height=600, background=vec(0.6,0.8,0.8),range = 0.9*R)
scene.center = vec(0,0,0)					#設定視窗中心點
ball = sphere(pos=vector(0,0.5,0), radius = 0.5, color=color.green, v = vec(0,0,0), make_trail = True)

pre_ball_pos = vector(0,0,0)

#  利用List畫出360顆小球代表圓環
balllist = []  
for N in range(0,360,1):  
    balllist.append(sphere(pos=vector(R*cos(N*pi/180),0,R*sin(N*pi/180)),
                           radius = 0.1, color=color.red))
"""
    3. 執行迴圈
"""
while True:
    rate (1000)

    pre_pre_ball_pos = pre_ball_pos
    pre_ball_pos = vector(ball.pos.x , ball.pos.y, ball.pos.z)

    t = t+dt

    Fglist=[]  #定義List
    for P in range(0,360,1):  #用for迴圈計算每個紅球與綠球間的距離與計算引力
        dist = ((ball.pos.x-balllist[P].pos.x)**2+(ball.pos.y-balllist[P].pos.y)**2+(ball.pos.z-balllist[P].pos.z)**2)**0.5
        radiavector = (ball.pos-balllist[P].pos)/dist
        Fglist.append(-G*M*m*radiavector/(dist**2))

    Fg = vector(0, 0, 0)          #每次迴圈重新計算要歸0
    for K in range(0,360,1):  #利用for迴圈將Fglist內儲存的力累加起來
        Fg += Fglist[K]
        
    ball.v += Fg/m*dt  #有力後就能改變速度與控制位置
    ball.pos = ball.pos + ball.v*dt

    if pre_ball_pos.y > pre_pre_ball_pos.y and pre_ball_pos.y > ball.pos.y :
        tp = 2*pi*((R**3)/(G*360*M))**0.5
        print ('simulate period = ' , '%1.5f'%t , 'theory period = ' , '%1.5f'%tp)  
        t = 0
