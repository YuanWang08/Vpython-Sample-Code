from vpython import *  
"""
    1. 參數設定，設定變數及定義萬有引力公式
"""
G = 6.67*10**(-11) ; M = 6*10**24 ; m = 1000  
Re = 6.4*10**6 ; H = 5*Re ; t = 0 ; dt = 1
V0 = (G*M/H)**0.5
def Fg(x):                                 #定義公式
    return -G*M*m/(x**2)
pre_mater_pos = vector(0,0,0)
sum_area=0
"""
    2. 畫面設定
"""
scene = canvas(align = 'left',title ='4_01_Gravity force',  width=800, height=300, center=vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(H,0,0), radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星
materv = vec(0,0.7*V0,0) #衛星速率=0

oval = curve( color = color.black )
for N in range(0, 360, 1):
    oval.append( pos =(2.119*10**7*cos(N*pi/180)+1*(2.119**2-1.8228**2)**0.5*10**7,1.8228*10**7*sin(N*pi/180),0) )
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

    pre_pre_mater_pos = pre_mater_pos
    pre_mater_pos = vector(mater.pos.x , mater.pos.y, mater.pos.z)
    
    dist = ((mater.pos.x-earth.pos.x)**2+(mater.pos.y-earth.pos.y)**2+(mater.pos.z-earth.pos.z)**2)**0.5 #距離純量
    radiavector = (mater.pos-earth.pos)/dist #距離單位向量
    Fg_vector = Fg(dist)*radiavector # 萬有引力向量=萬有引力量值*單位向量
    
    materv += Fg_vector/m*dt   #Δv = F/m *dt
    mater.pos = mater.pos + materv*dt  # S = S0 + v *dt
  
    t = t+dt

    if pre_mater_pos.x > pre_pre_mater_pos.x and pre_mater_pos.x > mater.pos.x :
       print (mater.pos) #印出右端點
    if pre_mater_pos.x < pre_pre_mater_pos.x and pre_mater_pos.x < mater.pos.x : 
       print (mater.pos) #印出左端點
    if pre_mater_pos.y > pre_pre_mater_pos.y and pre_mater_pos.y > mater.pos.y :
       print (mater.pos) #印出上端點
    if pre_mater_pos.y < pre_pre_mater_pos.y and pre_mater_pos.y < mater.pos.y :
       print (mater.pos) #印出下端點

    a = mag(mater.pos-earth.pos)  #定義三角形的三邊長
    b = mag(earth.pos-pre_mater_pos)
    c = mag(pre_mater_pos-mater.pos)
    s = (a+b+c)/2        
    area = (s*(s-a)*(s-b)*(s-c))**0.5#用海龍公式計算面積
    sum_area += area            #累加每dt時刻內的面積，計算總面積
    if t >= 2785 :
        print (t , sum_area)
        t = 0
        sum_area = 0
        cylinder(pos=earth.pos, axis=mater.pos-earth.pos, radius=0.01*Re, color=color.black)  #每2785秒將地球與衛星之間連線繪圖
        
   # f1.plot( pos=(mater.pos.x/Re,mag(Fg_vector)/Fe))
"""
    4.當衛星碰觸地球表面，則衛星停止不動

while True:  
    rate(1000)
    materv = vector(0,0,0)
    mater.pos = mater.pos
"""


    
