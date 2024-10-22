from vpython import *  #引用視覺畫套件Vpython
G = 6.67 
m1=10
m2=10
m3=10
m=10
R=10
t = 0
dt = 0.001
L=10*(3**0.5)
v0=(G*m/L)**0.5
def Fg(x): 
    return -G*m**2/(x**2)

scene = canvas(width=1200, height=800, center=vec(0,0,0),background=vec(0.6,0.8,0.8),range=2*R)


ball_m1 = sphere(pos=vec(0,R,0), radius=0.2, color = color.yellow, make_trail=True)
ball_m2 = sphere(pos=vec(R*cos(pi/6),-R*sin(pi/6),0), radius=0.2, color = color.red, make_trail=True)
ball_m3 = sphere(pos=vec(-R*cos(pi/6),-R*sin(pi/6),0), radius=0.2, color = color.blue, make_trail=True)

ball_m1_v = vector(-v0,0,0)  
ball_m2_v = vector(v0*cos(pi/3),v0*sin(pi/3),0)
ball_m3_v = vector(v0*cos(pi/3),-v0*sin(pi/3),0)

F1_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.black)
F13_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.blue)
F12_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.red)
v1_arrow = arrow(pos=ball_m1.pos,axis=vec(0,0,0),shaftwidth=0.1 ,color = color.yellow)
"""
    3. 執行迴圈
"""
while True:
    rate(1000)
    dist_12 = mag(ball_m1.pos - ball_m2.pos)
    radiavector_12 = (ball_m1.pos-ball_m2.pos)/dist_12
    Fg_vector_12 = Fg(dist_12)*radiavector_12
    
    dist_31 = mag(ball_m3.pos - ball_m1.pos)
    radiavector_31 = (ball_m3.pos-ball_m1.pos)/dist_31
    Fg_vector_31 = Fg(dist_31)*radiavector_31

    dist_23 = mag(ball_m2.pos - ball_m3.pos)
    radiavector_23 = (ball_m2.pos-ball_m3.pos)/dist_23
    Fg_vector_23 = Fg(dist_23)*radiavector_23
    
    ball_m1_v += (-Fg_vector_31+Fg_vector_12)/m1*dt #
    ball_m1.pos = ball_m1.pos + ball_m1_v*dt

    ball_m2_v += (-Fg_vector_12+Fg_vector_23)/m2*dt #
    ball_m2.pos = ball_m2.pos + ball_m2_v*dt

    ball_m3_v += (-Fg_vector_23+Fg_vector_31)/m3*dt #
    ball_m3.pos = ball_m3.pos + ball_m3_v*dt

    F1_arrow.pos = ball_m1.pos
    F1_arrow.axis = (-Fg_vector_31+Fg_vector_12)

    F13_arrow.pos = ball_m1.pos
    F13_arrow.axis = (-Fg_vector_31)

    F12_arrow.pos = ball_m1.pos
    F12_arrow.axis = (Fg_vector_12)

    v1_arrow.pos = ball_m1.pos
    v1_arrow.axis = ball_m1_v
