from vpython import* 

theta = 00.0 * pi / 180 #粒子入射角度, 改為平行入射
per_N = 5.0             #每秒射出的粒子數,改為每秒射入5個粒子
k = 9*10**9             #設定庫倫常數

Q_charge = 10**(-5)     
q_charge = 10 **(-8)    
q_m = 10**(-3)          

d = 3.0                 
r = 0.5                 
v0 = 2.0                

t = 0.0               
t1 = 0.0
dt = 0.0001 

scene = canvas(align = 'left',title ='指定作業09-2', center = vec ( -0.5*d, 0 , 0 ) , height=600, width=1000, range=3.5,auto_scale=False, background=vec(0.6,0.8,0.8) , fov = 0.004)  #設定畫面
Q = sphere(pos = vec(0,0,0) ,  radius = 0.2 , color = color.yellow)                                                                                              

def Force_E(r, q):      
    r1 = r - Q.pos
    return k*q*Q_charge*r1.norm()/(r1.mag*r1.mag)             

alpha = []              

while True:
    rate(10000)
    t = t + dt 
    t1 = t1 + dt  

    if t1 > 1/ per_N:   
        t1 = 0
        r_dom = random()
        p_dom = random()
        alpha.append( sphere(pos = vector((-d*cos(theta)+r*r_dom*cos(p_dom*2*pi)*sin(theta)), (d*sin(theta)+r*r_dom*cos(p_dom*2*pi)*cos(theta)),(r*r_dom*sin(p_dom*2*pi))) , radius = 0.05, v = vec(v0*cos(theta),-v0*sin(theta),0), Fx = 0 , visible = True, make_trail = True))

    for N in alpha :                  
        N.v = N.v + Force_E(N.pos, q_charge)/q_m *dt
        N.pos = N.pos+N.v*dt
        
        if mag(N.pos - vec(0,0,0)) > 4: 
            N.visible = False
            N = None
