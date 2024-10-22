from vpython import *  

G = 6.67*10**(-11)
M = 6*10**24
m = 1000  
Re = 6.4*10**6
H1 = 7*Re
H2 = 9*Re
v01=(G*M/H1)**0.5
v02=(G*M/H2)**0.5
t1 = 0
t2 = 0
dt = 1

def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)


scene = canvas(align = 'left',title ='Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗

sun = sphere(pos=vec(0,0,0), radius=Re,color=color.yellow) #放置物件衛星
venus = sphere(pos=vec(H1,0,0), radius=0.1*Re,color=color.orange,make_trail=True)
earth = sphere(pos=vec(H2,0,0), radius=0.1*Re,texture=textures.earth,make_trail=True) 

venus.v=vec(0,0.8*v01,0)
earth.v=vec(0,0.8*v02,0)

pre_pre1=venus.pos.x
pre_pre2=earth.pos.x

while True:  #執行迴圈
    rate(5000)
    pre1=venus.pos.x
    pre2=earth.pos.x

    
    dist1 = (mag(venus.pos-sun.pos))
    radiavector1 =norm(venus.pos-sun.pos) #距離單位向量
    Fg_vector1 = Fg(dist1)*radiavector1 # 萬有引力向量=萬有引力量值*單位向量

    dist2 = (mag(earth.pos-sun.pos))
    radiavector2 =norm(earth.pos-sun.pos) #距離單位向量
    Fg_vector2 = Fg(dist2)*radiavector2 # 萬有引力向量=萬有引力量值*單位向量

    venus.v = venus.v + Fg_vector1/m*dt
    venus.pos = venus.pos + venus.v*dt
    earth.v = earth.v + Fg_vector2/m*dt
    earth.pos = earth.pos + earth.v*dt

    t1=t1+dt
    t2=t2+dt
    
    if pre_pre1>pre1 and venus.pos.x>pre1:
        left1=venus.pos.x
    if pre_pre1<pre1 and venus.pos.x<pre1:
        right1=venus.pos.x
        r1=(abs(right1)+abs(left1))/2
        print (' k1 = r1^3/T1^3 = ', r1**3/t1**2) #列印結果
        t1=0.0

    if pre_pre2>pre2 and earth.pos.x>pre2:
        left2=earth.pos.x
    if pre_pre2<pre2 and earth.pos.x<pre2:
        right2=earth.pos.x
        r2=(abs(right2)+abs(left2))/2
        print (' k2 = r2^3/T2^3 = ', r2**3/t2**2) #列印結果
        t2=0.0
  
