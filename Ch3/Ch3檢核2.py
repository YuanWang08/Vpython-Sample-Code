from vpython import *
g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000                  #彈簧力常數 10 N/m
m = 0.1                 #球質量 0.1 kg
Fg = m*vector(0,-g,0)   #球所受重力向量
theta=30*pi/180
damp=1
def SpringForce(r,L):
    return -k*(mag(r)-L)*r/mag(r)
def SpringDamp(v, r):  #避震器
    cos_theta = dot(v,r)/(mag(v)*mag(r))                    #用向量內積找v和r夾角的餘弦函數
    r_unit_vector = norm(r)                                 #沿彈簧軸方向的單位向量
    projection_vector = mag(v) * cos_theta * r_unit_vector  #計算v在r方向的分量
    spring_damp = - damp * projection_vector                #沿彈簧軸方向的阻力
    return spring_damp

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
spring = cylinder(radius=size/20)#畫彈簧

v_text = label(box = False, opacity = 0, height = 25, color=color.green, text = 'v')  #產生文字標籤'v'
a_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'a')  #產生文字標籤'a'


v_vector=arrow(color=color.green,shaftwidth=0.02)
Fs_vector=arrow(color=color.white,shaftwidth=0.02)
mg_vector=arrow(color=color.yellow,shaftwidth=0.02)
F_tot_vector=arrow(color=color.red,shaftwidth=0.02)
X=0.4

ball.pos = vector(L*sin(theta), -L*cos(theta), 0)     #球在t=0時的位置
vz=(g*L*sin(theta)*tan(theta))**0.5
ball.v = vector(0, 0, vz)        #球初速
spring.pos = vector(0, 0, 0)    #彈簧頭端的位置

dt = 0.001
t=0
pre_x=ball.pos.x


while True:
    rate(1/dt)
    spring.axis = ball.pos - spring.pos           #彈簧的軸方向，由頭端指向尾端的距離向量
    ball.a = (Fg + SpringForce(spring.axis,L)+SpringDamp(ball.v,spring.axis))/m  #球的加速度由重力和彈力所造成
    ball.v += ball.a*dt      #球的速度

    pre_pre_x=pre_x
    pre_x=ball.pos.x
    ball.pos += ball.v*dt    #球的位置

    if pre_x>pre_pre_x and pre_x>ball.pos.x:
        print('simu.period=',t,'tp=',2*pi*((L*cos(theta)/g)**0.5))
        t=0
        
    t=t+dt
    
    v_vector.pos=Fs_vector.pos=mg_vector.pos=F_tot_vector.pos=ball.pos
    v_vector.axis=ball.v*X
    Fs_vector.axis=SpringForce(spring.axis,L)*X
    mg_vector.axis=Fg*X
    F_tot_vector.axis=m*ball.a*X
    

