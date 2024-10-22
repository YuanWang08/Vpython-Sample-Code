from vpython import *  
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
V0 = (G*M/H)**0.5
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)

"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.yellow, make_trail=True) #放置物件衛星
materv = vec(0,0.7*V0,0) #衛星速率=0

v_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.red)
a_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.4*mater.radius ,color = color.yellow)

aT_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.black)
aN_arrow = arrow(pos=mater.pos,axis=vec(0,0,0),shaftwidth=0.6*mater.radius ,color = color.blue)



"""
gd = graph(align='left',width=400,height=400,  #設定X-t繪圖視窗
              title='Fg', xtitle='R', ytitle='Fg(red)',
              foreground=color.black,background=color.white,
              xmax=20, xmin=-2, ymax=1.2, ymin=0)
f1 = gcurve(color=color.red)  #定義曲線
Fe = G*M*m/Re**2 #定義地球表面重力強度
"""
"""
    3. 執行迴圈
"""
while True:  #執行迴圈
    rate(5000)

   
    
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt
    
    v_arrow.pos = mater.pos
    v_arrow.axis = materv*2*10**3 #乘2*10**3  #為了讓動畫的速度向量顯著
    a_arrow.pos = mater.pos
    a_arrow.axis = Fg_vector/m*5*10**6 #乘  5*10**6  #可自行調整大小

    aT_arrow.pos = mater.pos
    aT_arrow.axis = dot(Fg_vector/m,materv)*(norm(materv)/mag(materv))*5*10**6
    aN_arrow.pos = mater.pos
    aN_arrow.axis = (mag(cross(Fg_vector/m,materv))/mag(materv))*cross(norm(materv),vector(0,0,-1))*5*10**6
  
    t = t+dt

    
   # f1.plot( pos=(mater.pos.x/Re,mag(Fg_vector)/Fe))
"""
    4.當衛星碰觸地球表面，則衛星停止不動

while True:  
    rate(1000)
    materv = vector(0,0,0)
    mater.pos = mater.pos
"""


    
