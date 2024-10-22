from vpython import*
"""
    1. 參數設定
"""
m1 = 1
m2 = 5
m3 = 30
g= 9.8
dt = 0.001
t=0
size1 = 1
size2 = 2
size3 = 3
height_1 = 20.0
height_2 = 17.0
height_3 = 12.0       

"""
    2. 畫面設定
"""

scene = canvas(width=400, height=600,center = vec(0,height_1,0), background=vec(0.6,0.8,0.8)) #設定畫面
floor = box(length=15, height=0.01, width=10, color=color.blue)                         #畫地板
ball_1 = sphere(pos = vec( 0, height_1, 0), v = vec(0,0,0) , radius = size1, color=color.yellow ) #畫球
ball_2 = sphere(pos = vec( 0, height_2, 0), v = vec(0,0,0) , radius = size2, color=color.green ) #畫球
ball_3 = sphere(pos = vec( 0, height_3, 0), v = vec(0,0,0) , radius = size3, color=color.blue ) #畫球

pre_pos = ball_1.pos.y
now_pos=ball_1.pos.y

"""
    3. 執行迴圈
"""
while True:             
    rate(1000)  
    t=t+dt
    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt
    if ball_1.pos.y<=size1 and ball_1.v.y<0:
        ball_1.v.y=-1*ball_1.v.y

    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    if ball_2.pos.y<=size2 and ball_2.v.y<0:
        ball_2.v.y=-1*ball_1.v.y
        
    ball_3.pos += ball_3.v*dt
    ball_3.v.y += - g*dt
    if ball_3.pos.y<=size3 and ball_3.v.y<0:
        ball_3.v.y=-1*ball_3.v.y
        
    if mag(ball_1.pos-ball_2.pos)<=size1+size2:
        v1y=(m1-m2)*ball_1.v.y/(m1+m2)+2*m2*ball_2.v.y/(m1+m2)
        v2y=(m1-m2)*ball_2.v.y/(m1+m2)+2*m2*ball_1.v.y/(m1+m2)
        ball_1.v=vector(0,v1y,0)
        ball_2.v=vector(0,v2y,0)
    if mag(ball_2.pos-ball_3.pos)<=size3+size2:
        v2y=(m2-m3)*ball_2.v.y/(m2+m3)+2*m2*ball_3.v.y/(m2+m3)
        v3y=(m2-m3)*ball_3.v.y/(m2+m3)+2*m2*ball_2.v.y/(m2+m3)
        ball_2.v=vector(0,v2y,0)
        ball_3.v=vector(0,v3y,0)

    pre_pre_pos=pre_pos
    pre_pos=now_pos
    now_pos=ball_1.pos.y+ball_1.v.y*dt
        
    if pre_pre_pos < pre_pos and now_pos < pre_pos and t>2 :
        print (now_pos)
    if ball_3.pos.y <= size3 and ball_3.v.y < 0:   
        ball_3.v.y = - 1* ball_3.v.y
