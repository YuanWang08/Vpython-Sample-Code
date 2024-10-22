from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size =0.05     
L = 0.5                 
k = 100000               
m = 0.1                 #球質量 0.1 kg
Fg = m*vector(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0),range=1.2*L)#設定畫面
mark_ball= sphere(radius = size,  color=color.yellow, pos=vector(0,0,0))#畫球
ball_1 = sphere(radius = size,  color=color.red, make_trail = False, retain = 1000, interval=1)#畫球
ball_2 = sphere(radius = size,  color=color.green, make_trail = False, retain = 1000, interval=1)#畫球

gd1=graph(title='E-t plot',width=600,height=400,xtitle='t',ytitle='E')
f1=gcurve(color=color.green)
f2=gcurve(color=color.red)
f3=gcurve(color=color.blue)

rod_1 = cylinder(pos=vector(0,0,0), radius=size/10)
rod_2 = cylinder(pos=vector(L,0,0), radius=size/10)
ball_1.pos= vector(L,0,0)
ball_2.pos= vector(2*L,0,0)            

ball_1.v = vector(0.0000001, 0, 0)        #球初速
ball_2.v = vector(0.0000001, 0, 0)

t=0.0
dt = 0.001

while True:
    rate(1/dt)
    t=t+dt

    rod_2.pos = ball_1.pos                 #外棒的位子在紅球處
    rod_1.axis = ball_1.pos                #內棒的軸方向由原點指向紅球
    rod_2.axis = ball_2.pos - ball_1.pos   #外棒的軸方向由紅球指向綠球

    ball_1.a = (Fg + SpringForce(rod_1.axis,L) - SpringForce(rod_2.axis,L))/m
    ball_2.a = (Fg + SpringForce(rod_2.axis,L))/m
    
    ball_1.v += ball_1.a*dt
    ball_1.pos += ball_1.v*dt
    ball_2.v += ball_2.a*dt
    ball_2.pos += ball_2.v*dt

    F1=m * g * ball_1.pos.y + 0.5*k*(mag(rod_1.axis)-L)**2+0.5*m*mag(ball_1.v)**2
    F2=m * g * ball_2.pos.y + 0.5*k*(mag(rod_2.axis)-L)**2+0.5*m*mag(ball_2.v)**2

    f1.plot(pos=(t,F2))
    f2.plot(pos=(t,F1))
    f3.plot(pos=(t,F1+F2))
    
    
