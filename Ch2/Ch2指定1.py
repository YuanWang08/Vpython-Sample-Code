from vpython import*

g=9.8
size=1.0
height=15.0
m=1.0
Fg=vector(0,-m*g,0)


ball=sphere(color=color.yellow,radius=size,make_trail=True,trail_type="points",interval=100)
ball2=sphere(color=color.red,radius=size,make_trail=True,trail_type="points",interval=100)
scene=canvas(width=2500,height=600,x=0,y=0,center=vector(0,height/2,0))
ball3=sphere(color=color.blue,pos=vector(0,0,8),radius=5.0)

ball.pos=vector(0,size,0)
ball.v=vector(10,10,0)

ball2.pos=vector(0,size,2)
ball2.v=vector(10,10,0)

dt=0.001
t=0
damp=0.4

while True:
    rate(1/dt)  #ball
    t=t+dt
    
    ball.a=Fg/m
    ball.v=ball.v+ball.a*dt
    ball.pos=ball.pos+ball.v*dt
    if ball.pos.y >=size and ball.pos.y+ball.v.y*dt <= size:    
        ball.v=vector(0,0,0)
    if ball.pos.y<size:
        ball.pos.y=size
    #ball2
    ball2.a=(-damp*ball2.v+Fg)/m
    ball2.v=ball2.v+ball2.a*dt
    ball2.pos=ball2.pos+ball2.v*dt
    if ball2.pos.y >=size and ball2.pos.y+ball2.v.y*dt <= size:    
        ball2.v=vector(0,0,0)
    if ball2.pos.y<size:
        ball2.pos.y=size
    
