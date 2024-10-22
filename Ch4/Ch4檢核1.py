"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/07/25
    特色課程 Lecture 04 碰撞
    4_01_1D_collision_constant force.py

"""
from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
m1 = 2.0                   #球1質量
x1 = -20.0                  #球1X軸初位置
v1= 6.0                    #球1初速度
size1 = 1.0                 #球1大小

m2 = 1.0                   #球2質量
x2 = -5.0                   #球2X軸初位置
v2= 3.0                    #球2初速度
size2 = 1.0                 #球2大小

##Force = 5.0               #彈力大小
spring_k=2.0
spring_L = 5.0             #彈簧長度 

"""
    2. 畫面設定
"""

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10),forward=vec(0,0,-1),range=10, fov=0.004)#設定畫面
ball1 = sphere(radius=size1, color = color.red, make_trail = False)  #設定球1
ball1.pos = vector(x1,0,0)             #球1位置
ball1.v = vector (v1,0,0)                        #球1的速度
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(radius=size2, color = color.blue,make_trail = False) #設定球2
ball2.pos = vector(x2,0,0)             #球2位置
ball2.v = vector (v2,0,0)                        #球2的速度
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

spring = helix(pos=ball2.pos, radius=0.5, thickness =0.1) #畫彈簧
spring.coils = 10
spring.axis = vector(-spring_L,0,0)

t = 0                                            #時間
dt = 0.001                                       #單位時間
E_t = graph(align='left',width=333,height=300,   #畫E-t圖                                   
              title='K-purple , U-green , E-black', xtitle='t', ytitle='E',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=45, ymin=0)
f4_1 = gcurve(color=color.purple)
f4_2 = gcurve(color=color.green) 
f4_3 = gcurve(color=color.black) 

P_t = graph(align='left',width=333,height=300,   #畫P-t圖                                   
              title='P1-red , P2-blue , P-black', xtitle='t', ytitle='P',
              foreground=color.black,background=color.white,
              xmax=8, xmin=0, ymax=20, ymin=0)
f5_1 = gcurve(color=color.red)
f5_2 = gcurve(color=color.blue) 
f5_3 = gcurve(color=color.black)

"""
    3. 執行迴圈
"""

while True :
    rate(1000)

    ball1.pos = ball1.pos+ball1.v*dt  #控制球1的運動
    ball2.pos = ball2.pos+ball2.v*dt #控制球2的運動

    v1_arrow.pos = ball1.pos #球1速度向量箭頭的起始點在球1上
    v1_arrow.axis = ball1.v  #球1速度向量箭頭的長度與方向等於球1速度

    v2_arrow.pos =ball2.pos#球2速度向量箭頭的起始點在球2上
    v2_arrow.axis = ball2.v #球1速度向量箭頭的長度與方向等於球2速度

    spring.pos=ball2.pos #彈簧的起始點位置在球2上

    t=t+dt
    if mag(ball2.pos - ball1.pos) <= spring_L :
        ball1_a = -1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m1
        ball2_a = 1 * norm(ball2.pos-ball1.pos) * spring_k * (spring_L - mag( ball2.pos - ball1.pos )) / m2
        spring.axis = ball1.pos-ball2.pos 
    else :                             #如果沒有，兩球的加速度均為0
        ball1_a = vector(0,0,0)
        ball2_a = vector(0,0,0)
        spring.axis = vector(-spring_L,0,0)

    ball1.v = ball1.v + ball1_a*dt  #加速度是向量，所以要用vector(ball1_a,0,0)
    ball2.v = ball2.v + ball2_a*dt 
    K = 0.5*m1*ball1.v.x**2 + 0.5*m2*ball2.v.x**2 
    U = 0.5*spring_k*(spring_L - mag(spring.axis))**2
    E = K+U
    
    P1 = m1*ball1.v.x
    P2 = m2*ball2.v.x
    P = P1+P2
    f4_1.plot( pos=(t,K))
    f4_2.plot( pos=(t,U))
    f4_3.plot( pos=(t,E))

    f5_1.plot( pos=(t,P1))
    f5_2.plot( pos=(t,P2))
    f5_3.plot( pos=(t,P))
