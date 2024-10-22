from vpython import*

k = 9*10**9                     #庫倫常數
size = 0.1                      #電荷球體大小
b_N = 36                        #表示電力線之球數

Q1_charge = 10**(-5)             
Q1_position = vector(-2, 0, 0)  
Q2_charge = -1*10**(-5)          
Q2_position = vector(0, 2, 0)   
Q3_charge = 10**(-5)             
Q3_position = vector(2, 0, 0)   
Q4_charge = -1*10**(-5)          
Q4_position = vector(0, -2, 0)

q_charge = 1 * 10 **(-7)        
q_position = vector (2 , 2 , 0) 
q_m = 10**(-3)                    
q_v = vector (0.0 , 0.0 , 0.0)

t = 0
dt = 0.001

scene = canvas(title ='指定作業09-1', height=600, width=1200, range=3.5, auto_scale=False, background=vec(0.3,0.4,0.4), fov=0.004)
Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos = Q2_position , radius = size , color = color.red)
Q3 = sphere(pos = Q3_position , radius = size , color = color.blue)
Q4 = sphere(pos = Q4_position , radius = size , color = color.red)
q = sphere(pos = q_position , radius = 0.5*size , color = color.green , v = q_v, make_trail=True)

field_ball_1=[]
for N in range(0,b_N,1):
    field_ball_1.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q1_position,radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))
field_ball_2=[]
for N in range(0,b_N,1):
    field_ball_2.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q2_position,radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))
field_ball_3=[]
for N in range(0,b_N,1):
    field_ball_3.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q3_position,radius=0.01, color=vec(1,1,0), make_trail=True, v=vector(0,0,0)))
field_ball_4=[]
for N in range(0,b_N,1):
    field_ball_4.append(sphere(pos=vector(size*cos(2*pi*N/b_N), size*sin(2*pi*N/b_N),0)+Q4_position,radius=0.01, color=vec(0.8,0.8,0.3), make_trail=True, v=vector(0,0,0)))
    
#設定小綠球受電磁力之函式
def Force_E(r, q):
    r1 = r - Q1_position
    r2 = r - Q2_position
    r3 = r - Q3_position
    r4 = r - Q4_position
    return k*q*Q1_charge*r1.norm()/(r1.mag**2)+k*q*Q2_charge*r2.norm()/(r2.mag**2)+k*q*Q3_charge*r3.norm()/(r3.mag**2)+k*q*Q4_charge*r4.norm()/(r4.mag**2)

while True:
    rate(1000)
    
    for N in field_ball_1: #設定Q1電力線
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_2: #設定Q2電力線
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_3: #設定Q3電力線
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    for N in field_ball_4: #設定Q4電力線
        N.v = Force_E(N.pos, 1.0).norm()
        N.pos += N.v*dt

    if mag(q.pos-Q1_position)>=size and mag(q.pos-Q2_position)>=size :    
        q.v = q.v + Force_E(q.pos, q_charge)/q_m *dt
        q.pos = q.pos+q.v*dt
    else :
        q.pos = q.pos
