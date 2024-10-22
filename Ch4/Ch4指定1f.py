from vpython import*
m1 = 1
m2 = 5
m3 = 30
g= 9.8 
dt = 0.001                
size1 = 1
size2 = 2 
size3 = 3
height_1 = 20.0
height_2 = 17.0
height_3 = 12.0

scene = canvas(width=600, height=800,center = vec(0,height_1,0), background=vec(0.6,0.8,0.8)) #設定畫面
floor = box(length=40, height=0.01, width=10, color=color.blue)                         #畫地板
ball_1 = sphere(pos = vec( 0, height_1, 0), v = vec(0,0,0) , radius = size1, color=color.yellow ) #畫球
ball_2 = sphere(pos = vec( 0, height_2, 0), v = vec(0,0,0) , radius = size2, color=color.green ) #畫球
ball_3 = sphere(pos = vec( 0, height_3, 0), v = vec(0,0,0) , radius = size3, color=color.blue ) #畫球

pre_ball_1_pos = vector(0,0,0)

while True:             
    rate(1000)
    
    pre_pre_ball_1_pos = pre_ball_1_pos
    pre_ball_1_pos = vector(ball_1.pos.x , ball_1.pos.y, ball_1.pos.z)
    
    ball_1.pos += ball_1.v*dt
    ball_1.v.y += - g*dt
    
    ball_2.pos += ball_2.v*dt
    ball_2.v.y += - g*dt
    
    ball_3.pos += ball_3.v*dt
    ball_3.v.y += - g*dt
    
    if ball_3.pos.y <= size3 and ball_3.v.y < 0:   
        ball_3.v.y = - 1* ball_3.v.y
        
    if ball_2.pos.y-ball_3.pos.y <= size2+size3  and ball_2.v.y < 0:
        v2x = (m2-m3)*ball_2.v.y/(m2+m3) + 2*m3*ball_3.v.y/(m2+m3)
        v3x = (m2-m3)*ball_3.v.y/(m2+m3) + 2*m2*ball_2.v.y/(m2+m3)       
        ball_2.v = vector (0,v2x , 0)
        ball_3.v = vector (0,v3x , 0)
        
    if ball_1.pos.y-ball_2.pos.y <= size2+size1  and ball_1.v.y < 0:
        v1x = (m1-m2)*ball_1.v.y/(m1+m2) + 2*m2*ball_2.v.y/(m1+m2)
        v2x = (m1-m1)*ball_2.v.y/(m1+m2) + 2*m1*ball_1.v.y/(m1+m2)       
        ball_1.v = vector (0,v1x , 0)
        ball_2.v = vector (0,v2x , 0)
        
    if pre_ball_1_pos.y > pre_pre_ball_1_pos.y and pre_ball_1_pos.y > ball_1.pos.y :
        print (ball_1.pos.y)
