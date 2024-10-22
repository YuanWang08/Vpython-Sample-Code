from vpython import *  #引用視覺畫套件Vpython
"""
    1. 參數設定
"""
print('請先利用滾輪調整螢幕到一個適當的大小')
print('滑鼠點擊畫面可以拖曳紅色球桿')
print('在點擊球擊可射出')
L=107 #長
H=0.1  #高
W=213  #寬
scene = scene = canvas(background=color.white)
scene.center=vec(0,5.715,0)
scene.camera.pos=vec(0,250,0)
scene.camera.axis=vec(0,-30,0)
scene.up=vec(0,0,-1)
scene.center=vec(0,5.715,0)


size= 5.715  #球半徑

balldist=-size*(3**0.5)

vN=4.0
detnum=13.215

t=0
dt=0.001

ball0fall=0
ball1fall=0
ball2fall=0
ball3fall=0
ball4fall=0
ball5fall=0
ball6fall=0
ball7fall=0
ball8fall=0
ball9fall=0

m0=15.6
m1=15.6
m2=15.6
m3=15.6
m4=15.6
m5=15.6
m6=15.6
m7=15.6
m8=15.6
m9=15.6


v0=vec(0,0,0)       #First input
v1=vec(0,0,0)
v2=vec(0,0,0)
v3=vec(0,0,0)
v4=vec(0,0,0)
v5=vec(0,0,0)
v6=vec(0,0,0)
v7=vec(0,0,0)
v8=vec(0,0,0)
v9=vec(0,0,0)

r0=vector(0,size,53.5)
r1=vector(0,size,-38.5)
r2=vector(size,size,-38.5+balldist*1)
r3=vector(-size,size,-38.5+balldist*1)
r4=vector(2*size,size,-38.5+balldist*2)
r5=vector(0,size,-38.5+balldist*2)
r6=vector(-2*size,size,-38.5+balldist*2)
r7=vector(size,size,-38.5+balldist*3)
r8=vector(-size,size,-38.5+balldist*3)
r9=vector(0,size,-38.5+balldist*4)

ball_0=sphere(radius=size,pos=r0,color=color.white,v=v0)
ball_1=sphere(radius=size,pos=r1,color=color.yellow,v=v1)
ball_2=sphere(radius=size,pos=r2,color=color.blue,v=v2)
ball_3=sphere(radius=size,pos=r3,color=color.red,v=v3)
ball_4=sphere(radius=size,pos=r4,color=color.purple,v=v4)
ball_5=sphere(radius=size,pos=r5,color=color.orange,v=v5)
ball_6=sphere(radius=size,pos=r6,color=color.green,v=v6)
ball_7=sphere(radius=size,pos=r7,color=color.cyan,v=v7)
ball_8=sphere(radius=size,pos=r8,color=color.black,v=v8)
ball_9=sphere(radius=size,pos=r9,color=color.yellow,v=v9)


floor=box(pos=vector(0,0,0), length=L, height=H, width=W,color=color.yellow)
wall1=box(pos=vector(L/2,0,0), length=0.1, height=3, width=W,color=color.blue)
wall2=box(pos=vector(-L/2,0,0), length=0.1, height=3, width=W,color=color.blue)
wall3=box(pos=vector(0,0,W/2), length=L, height=3, width=0.1,color=color.blue)
wall4=box(pos=vector(0,0,-W/2), length=L, height=3, width=0.1,color=color.blue)

hp1=vector(-L/2,0,-W/2)
hp2=vector(L/2,0,-W/2)
hp3=vector(-L/2,0,W/2)
hp4=vector(L/2,0,W/2)
hp5=vector(L/2,0,0)
hp6=vector(-L/2,0,0)
hole1 = cylinder(pos=vector(-L/2,0,-W/2), axis=vector(0,3,0), radius= size +6,color=color.black)
hole2 = cylinder(pos=vector(L/2,0,-W/2), axis=vector(0,3,0), radius= size +6,color=color.black)
hole3 = cylinder(pos=vector(-L/2,0,W/2), axis=vector(0,3,0), radius= size +6,color=color.black)
hole4 = cylinder(pos=vector(L/2,0,W/2), axis=vector(0,3,0), radius= size +6,color=color.black)
hole5 = cylinder(pos=vector(L/2,0,0), axis=vector(0,3,0), radius= size +6,color=color.black)
hole6 = cylinder(pos=vector(-L/2,0,0), axis=vector(0,3,0), radius= size +6,color=color.black)

log = cylinder(pos=ball_0.pos, axis=vector(0,0,0), radius= 2,color=color.red)

det0=0
det1=0
det2=0
det3=0
det4=0
det5=0
det6=0
det7=0
det8=0
det9=0

got_0=0
got_0_t=0

by = 20.0 # touch this close to tail or tip, 滑鼠按下後與尾與箭頭的判斷距離
drag = None # have not selected tail or tip of arrow, 判斷是否選擇了尾與箭頭

    #碰撞函式(預計45組)

def three_D_col_for01(v0, v1, r0, r1):#1
    v0_col = v0 - (2*m1/(m0+m1))*dot((v0 - v1), (r0 - r1)) * (r0-r1) / mag2(r0 - r1) 
    v1_col = v1 - (2*m0/(m0+m1))*dot((v1 - v0), (r1 - r0)) * (r1-r0) / mag2(r1 - r0) 
    return (v0_col, v1_col)
def three_D_col_for02(v0, v2, r0, r2):#2
    v0_col = v0 - (2*m2/(m0+m2))*dot((v0 - v2), (r0 - r2)) * (r0-r2) / mag2(r0 - r2) 
    v2_col = v2 - (2*m0/(m0+m2))*dot((v2 - v0), (r2 - r0)) * (r2-r0) / mag2(r2 - r0) 
    return (v0_col, v2_col)
def three_D_col_for03(v0, v3, r0, r3):#3
    v0_col = v0 - (2*m3/(m0+m3))*dot((v0 - v3), (r0 - r3)) * (r0-r3) / mag2(r0 - r3) 
    v3_col = v3 - (2*m0/(m0+m3))*dot((v3 - v0), (r3 - r0)) * (r3-r0) / mag2(r3 - r0) 
    return (v0_col, v3_col)
def three_D_col_for04(v0, v4, r0, r4):#4
    v0_col = v0 - (2*m4/(m0+m4))*dot((v0 - v4), (r0 - r4)) * (r0-r4) / mag2(r0 - r4) 
    v4_col = v4 - (2*m0/(m0+m4))*dot((v4 - v0), (r4 - r0)) * (r4-r0) / mag2(r4 - r0) 
    return (v0_col, v4_col)
def three_D_col_for05(v0, v5, r0, r5):#5
    v0_col = v0 - (2*m5/(m0+m5))*dot((v0 - v5), (r0 - r5)) * (r0-r5) / mag2(r0 - r5) 
    v5_col = v5 - (2*m0/(m0+m5))*dot((v5 - v0), (r5 - r0)) * (r5-r0) / mag2(r5 - r0) 
    return (v0_col, v5_col)
def three_D_col_for06(v0, v6, r0, r6):#6
    v0_col = v0 - (2*m6/(m0+m6))*dot((v0 - v6), (r0 - r6)) * (r0-r6) / mag2(r0 - r6) 
    v6_col = v6 - (2*m0/(m0+m6))*dot((v6 - v0), (r6 - r0)) * (r6-r0) / mag2(r6 - r0) 
    return (v0_col, v6_col)
def three_D_col_for07(v0, v7, r0, r7):#7
    v0_col = v0 - (2*m7/(m0+m7))*dot((v0 - v7), (r0 - r7)) * (r0-r7) / mag2(r0 - r7) 
    v7_col = v7 - (2*m0/(m0+m7))*dot((v7 - v0), (r7 - r0)) * (r7-r0) / mag2(r7 - r0) 
    return (v0_col, v7_col)
def three_D_col_for08(v0, v8, r0, r8):#8
    v0_col = v0 - (2*m8/(m0+m8))*dot((v0 - v8), (r0 - r8)) * (r0-r8) / mag2(r0 - r8) 
    v8_col = v2 - (2*m0/(m0+m8))*dot((v8 - v0), (r8 - r0)) * (r8-r0) / mag2(r8 - r0) 
    return (v0_col, v8_col)
def three_D_col_for09(v0, v9, r0, r9):#9
    v0_col = v0 - (2*m9/(m0+m9))*dot((v0 - v9), (r0 - r9)) * (r0-r9) / mag2(r0 - r9) 
    v9_col = v9 - (2*m0/(m0+m9))*dot((v9 - v0), (r9 - r0)) * (r9-r0) / mag2(r9 - r0) 
    return (v0_col, v9_col)

def three_D_col_for12(v1, v2, r1, r2):#10
    v1_col = v1 - (2*m2/(m1+m2))*dot((v1 - v2), (r1 - r2)) * (r1-r2) / mag2(r1 - r2) 
    v2_col = v2 - (2*m1/(m1+m2))*dot((v2 - v1), (r2 - r1)) * (r2-r1) / mag2(r2 - r1) 
    return (v1_col, v2_col)
def three_D_col_for13(v1, v3, r1, r3):#11
    v1_col = v1 - (2*m3/(m1+m3))*dot((v1 - v3), (r1 - r3)) * (r1-r3) / mag2(r1 - r3) 
    v3_col = v3 - (2*m1/(m1+m3))*dot((v3 - v1), (r3 - r1)) * (r3-r1) / mag2(r3 - r1) 
    return (v1_col, v3_col)
def three_D_col_for14(v1, v4, r1, r4):#12
    v1_col = v1 - (2*m4/(m1+m4))*dot((v1 - v4), (r1 - r4)) * (r1-r4) / mag2(r1 - r4) 
    v4_col = v4 - (2*m1/(m1+m4))*dot((v4 - v1), (r4 - r1)) * (r4-r1) / mag2(r4 - r1) 
    return (v1_col, v4_col)
def three_D_col_for15(v1, v5, r1, r5):#13
    v1_col = v1 - (2*m5/(m1+m5))*dot((v1 - v5), (r1 - r5)) * (r1-r5) / mag2(r1 - r5) 
    v5_col = v5 - (2*m1/(m1+m5))*dot((v5 - v1), (r5 - r1)) * (r5-r1) / mag2(r5 - r1) 
    return (v1_col, v5_col)
def three_D_col_for16(v1, v6, r1, r6):#14
    v1_col = v1 - (2*m6/(m1+m6))*dot((v1 - v6), (r1 - r6)) * (r1-r6) / mag2(r1 - r6) 
    v6_col = v6 - (2*m1/(m1+m6))*dot((v6 - v1), (r6 - r1)) * (r6-r1) / mag2(r6 - r1) 
    return (v1_col, v6_col)
def three_D_col_for17(v1, v7, r1, r7):#15
    v1_col = v1 - (2*m7/(m1+m7))*dot((v1 - v7), (r1 - r7)) * (r1-r7) / mag2(r1 - r7) 
    v7_col = v7 - (2*m1/(m1+m7))*dot((v7 - v1), (r7 - r1)) * (r7-r1) / mag2(r7 - r1) 
    return (v1_col, v7_col)
def three_D_col_for18(v1, v8, r1, r8):#16
    v1_col = v1 - (2*m8/(m1+m8))*dot((v1 - v8), (r1 - r8)) * (r1-r8) / mag2(r1 - r8) 
    v8_col = v8 - (2*m1/(m1+m8))*dot((v8 - v1), (r8 - r1)) * (r8-r1) / mag2(r8 - r1) 
    return (v1_col, v8_col)
def three_D_col_for19(v1, v9, r1, r9):#17
    v1_col = v1 - (2*m9/(m1+m9))*dot((v1 - v9), (r1 - r9)) * (r1-r9) / mag2(r1 - r9) 
    v9_col = v9 - (2*m1/(m1+m9))*dot((v9 - v1), (r9 - r1)) * (r9-r1) / mag2(r9 - r1) 
    return (v1_col, v9_col)

def three_D_col_for23(v2, v3, r2, r3):#18
    v2_col = v2 - (2*m3/(m2+m3))*dot((v2 - v3), (r2 - r3)) * (r2-r3) / mag2(r2 - r3) 
    v3_col = v3 - (2*m2/(m2+m3))*dot((v3 - v2), (r3 - r2)) * (r3-r2) / mag2(r3 - r2) 
    return (v2_col, v3_col)
def three_D_col_for24(v2, v4, r2, r4):#19
    v2_col = v2 - (2*m4/(m2+m4))*dot((v2 - v4), (r2 - r4)) * (r2-r4) / mag2(r2 - r4) 
    v4_col = v4 - (2*m2/(m2+m4))*dot((v4 - v2), (r4 - r2)) * (r4-r2) / mag2(r4 - r2) 
    return (v2_col, v4_col)
def three_D_col_for25(v2, v5, r2, r5):#20
    v2_col = v2 - (2*m5/(m2+m5))*dot((v2 - v5), (r2 - r5)) * (r2-r5) / mag2(r2 - r5) 
    v5_col = v5 - (2*m2/(m2+m5))*dot((v5 - v2), (r5 - r2)) * (r5-r2) / mag2(r5 - r2) 
    return (v2_col, v5_col)
def three_D_col_for26(v2, v6, r2, r6):#21
    v2_col = v2 - (2*m6/(m2+m6))*dot((v2 - v6), (r2 - r6)) * (r2-r6) / mag2(r2 - r6) 
    v6_col = v6 - (2*m2/(m2+m6))*dot((v6 - v2), (r6 - r2)) * (r6-r2) / mag2(r6 - r2) 
    return (v2_col, v6_col)
def three_D_col_for27(v2, v7, r2, r7):#22
    v2_col = v2 - (2*m7/(m2+m7))*dot((v2 - v7), (r2 - r7)) * (r2-r7) / mag2(r2 - r7) 
    v7_col = v7 - (2*m2/(m2+m7))*dot((v7 - v2), (r7 - r2)) * (r7-r2) / mag2(r7 - r2) 
    return (v2_col, v7_col)
def three_D_col_for28(v2, v8, r2, r8):#23
    v2_col = v2 - (2*m8/(m2+m8))*dot((v2 - v8), (r2 - r8)) * (r2-r8) / mag2(r2 - r8) 
    v8_col = v8 - (2*m2/(m2+m8))*dot((v8 - v2), (r8 - r2)) * (r8-r2) / mag2(r8 - r2) 
    return (v2_col, v8_col)
def three_D_col_for29(v2, v9, r2, r9):#24
    v2_col = v2 - (2*m9/(m2+m9))*dot((v2 - v9), (r2 - r9)) * (r2-r9) / mag2(r2 - r9) 
    v9_col = v9 - (2*m2/(m2+m9))*dot((v9 - v2), (r9 - r2)) * (r9-r2) / mag2(r9 - r2) 
    return (v2_col, v9_col)

def three_D_col_for34(v3, v4, r3, r4):#25
    v3_col = v3 - (2*m4/(m3+m4))*dot((v3 - v4), (r3 - r4)) * (r3-r4) / mag2(r3 - r4) 
    v4_col = v4 - (2*m3/(m3+m4))*dot((v4 - v3), (r4 - r3)) * (r4-r3) / mag2(r4 - r3) 
    return (v3_col, v4_col)
def three_D_col_for35(v3, v5, r3, r5):#26
    v3_col = v3 - (2*m5/(m3+m5))*dot((v3 - v5), (r3 - r5)) * (r3-r5) / mag2(r3 - r5) 
    v5_col = v5 - (2*m3/(m3+m5))*dot((v5 - v3), (r5 - r3)) * (r5-r3) / mag2(r5 - r3) 
    return (v3_col, v5_col)
def three_D_col_for36(v3, v6, r3, r6):#27
    v3_col = v3 - (2*m6/(m3+m6))*dot((v3 - v6), (r3 - r6)) * (r3-r6) / mag2(r3 - r6) 
    v6_col = v6 - (2*m3/(m3+m6))*dot((v6 - v3), (r6 - r3)) * (r6-r3) / mag2(r6 - r3) 
    return (v3_col, v6_col)
def three_D_col_for37(v3, v7, r3, r7):#28
    v3_col = v3 - (2*m7/(m3+m7))*dot((v3 - v7), (r3 - r7)) * (r3-r7) / mag2(r3 - r7) 
    v7_col = v7 - (2*m3/(m3+m7))*dot((v7 - v3), (r7 - r3)) * (r7-r3) / mag2(r7 - r3) 
    return (v3_col, v7_col)
def three_D_col_for38(v3, v8, r3, r8):#29
    v3_col = v3 - (2*m8/(m3+m8))*dot((v3 - v8), (r3 - r8)) * (r3-r8) / mag2(r3 - r8) 
    v8_col = v8 - (2*m3/(m3+m8))*dot((v8 - v3), (r8 - r3)) * (r8-r3) / mag2(r8 - r3) 
    return (v3_col, v8_col)
def three_D_col_for39(v3, v9, r3, r9):#30
    v3_col = v3 - (2*m9/(m3+m9))*dot((v3 - v9), (r3 - r9)) * (r3-r9) / mag2(r3 - r9) 
    v9_col = v9 - (2*m3/(m3+m9))*dot((v9 - v3), (r9 - r3)) * (r9-r3) / mag2(r9 - r3) 
    return (v3_col, v9_col)

def three_D_col_for45(v4, v5, r4, r5):#31
    v4_col = v4 - (2*m5/(m4+m5))*dot((v4 - v5), (r4 - r5)) * (r4-r5) / mag2(r4 - r5) 
    v5_col = v5 - (2*m4/(m4+m5))*dot((v5 - v4), (r5 - r4)) * (r5-r4) / mag2(r5 - r4) 
    return (v4_col, v5_col)
def three_D_col_for46(v4, v6, r4, r6):#32
    v4_col = v4 - (2*m6/(m4+m6))*dot((v4 - v6), (r4 - r6)) * (r4-r6) / mag2(r4 - r6) 
    v6_col = v6 - (2*m4/(m4+m6))*dot((v6 - v4), (r6 - r4)) * (r6-r4) / mag2(r6 - r4) 
    return (v4_col, v6_col)
def three_D_col_for47(v4, v7, r4, r7):#33
    v4_col = v4 - (2*m7/(m4+m7))*dot((v4 - v7), (r4 - r7)) * (r4-r7) / mag2(r4 - r7) 
    v7_col = v7 - (2*m4/(m4+m7))*dot((v7 - v4), (r7 - r4)) * (r7-r4) / mag2(r7 - r4) 
    return (v4_col, v7_col)
def three_D_col_for48(v4, v8, r4, r8):#34
    v4_col = v4 - (2*m8/(m4+m8))*dot((v4 - v8), (r4 - r8)) * (r4-r8) / mag2(r4 - r8) 
    v8_col = v8 - (2*m4/(m4+m8))*dot((v8 - v4), (r8 - r4)) * (r8-r4) / mag2(r8 - r4) 
    return (v4_col, v8_col)
def three_D_col_for49(v4, v9, r4, r9):#35
    v4_col = v4 - (2*m9/(m4+m9))*dot((v4 - v9), (r4 - r9)) * (r4-r9) / mag2(r4 - r9) 
    v9_col = v9 - (2*m4/(m4+m9))*dot((v9 - v4), (r9 - r4)) * (r9-r4) / mag2(r9 - r4) 
    return (v4_col, v9_col)

def three_D_col_for56(v5, v6, r5, r6):#36
    v5_col = v5 - (2*m6/(m5+m6))*dot((v5 - v6), (r5 - r6)) * (r5-r6) / mag2(r5 - r6) 
    v6_col = v6 - (2*m5/(m5+m6))*dot((v6 - v5), (r6 - r5)) * (r6-r5) / mag2(r6 - r5) 
    return (v5_col, v6_col)
def three_D_col_for57(v5, v7, r5, r7):#37
    v5_col = v5 - (2*m7/(m5+m7))*dot((v5 - v7), (r5 - r7)) * (r5-r7) / mag2(r5 - r7) 
    v7_col = v7 - (2*m5/(m5+m7))*dot((v7 - v5), (r7 - r5)) * (r7-r5) / mag2(r7 - r5) 
    return (v5_col, v7_col)
def three_D_col_for58(v5, v8, r5, r8):#38
    v5_col = v5 - (2*m8/(m5+m8))*dot((v5 - v8), (r5 - r8)) * (r5-r8) / mag2(r5 - r8) 
    v8_col = v8 - (2*m5/(m5+m8))*dot((v8 - v5), (r8 - r5)) * (r8-r5) / mag2(r8 - r5) 
    return (v5_col, v8_col)
def three_D_col_for59(v5, v9, r5, r9):#39
    v5_col = v5 - (2*m9/(m5+m9))*dot((v5 - v9), (r5 - r9)) * (r5-r9) / mag2(r5 - r9) 
    v9_col = v9 - (2*m5/(m5+m9))*dot((v9 - v5), (r9 - r5)) * (r9-r5) / mag2(r9 - r5) 
    return (v5_col, v9_col)

def three_D_col_for67(v6, v7, r6, r7):#40
    v6_col = v6 - (2*m7/(m6+m7))*dot((v6 - v7), (r6 - r7)) * (r6-r7) / mag2(r6 - r7) 
    v7_col = v7 - (2*m6/(m6+m7))*dot((v7 - v6), (r7 - r6)) * (r7-r6) / mag2(r7 - r6) 
    return (v6_col, v7_col)
def three_D_col_for68(v6, v8, r6, r8):#41
    v6_col = v6 - (2*m8/(m6+m8))*dot((v6 - v8), (r6 - r8)) * (r6-r8) / mag2(r6 - r8) 
    v8_col = v8 - (2*m6/(m6+m8))*dot((v8 - v6), (r8 - r6)) * (r8-r6) / mag2(r8 - r6) 
    return (v6_col, v8_col)
def three_D_col_for69(v6, v9, r6, r9):#42
    v6_col = v6 - (2*m9/(m6+m9))*dot((v6 - v9), (r6 - r9)) * (r6-r9) / mag2(r6 - r9) 
    v9_col = v9 - (2*m6/(m6+m9))*dot((v9 - v6), (r9 - r6)) * (r9-r6) / mag2(r9 - r6) 
    return (v6_col, v9_col)

def three_D_col_for78(v7, v8, r7, r8):#43
    v7_col = v7 - (2*m8/(m7+m8))*dot((v7 - v8), (r7 - r8)) * (r7-r8) / mag2(r7 - r8) 
    v8_col = v8 - (2*m7/(m7+m8))*dot((v8 - v7), (r8 - r7)) * (r8-r7) / mag2(r8 - r7) 
    return (v7_col, v8_col)
def three_D_col_for79(v7, v9, r7, r9):#44
    v7_col = v7 - (2*m9/(m7+m9))*dot((v7 - v9), (r7 - r9)) * (r7-r9) / mag2(r7 - r9) 
    v9_col = v9 - (2*m7/(m7+m9))*dot((v9 - v7), (r9 - r7)) * (r9-r7) / mag2(r9 - r7) 
    return (v7_col, v9_col)

def three_D_col_for89(v8, v9, r8, r9):#45
    v8_col = v8 - (2*m9/(m8+m9))*dot((v8 - v9), (r8 - r9)) * (r8-r9) / mag2(r8 - r9) 
    v9_col = v9 - (2*m8/(m8+m9))*dot((v9 - v8), (r9 - r8)) * (r9-r8) / mag2(r9 - r8) 
    return (v8_col, v9_col)


while True:
    while True:
        rate(3000)

        t=t+dt
        
        ball_0.pos = ball_0.pos + ball_0.v*dt
        ball_1.pos = ball_1.pos + ball_1.v*dt
        ball_2.pos = ball_2.pos + ball_2.v*dt
        ball_3.pos = ball_3.pos + ball_3.v*dt
        ball_4.pos = ball_4.pos + ball_4.v*dt
        ball_5.pos = ball_5.pos + ball_5.v*dt
        ball_6.pos = ball_6.pos + ball_6.v*dt
        ball_7.pos = ball_7.pos + ball_7.v*dt
        ball_8.pos = ball_8.pos + ball_8.v*dt
        ball_9.pos = ball_9.pos + ball_9.v*dt
        

        #偵測是否發生球與球的碰撞(預計45組)
        
        if mag(ball_0.pos - ball_1.pos) <= 2*size and dot(ball_0.pos - ball_1.pos,ball_0.v-ball_1.v) < 0:
            ball_0.v, ball_1.v = three_D_col_for01(ball_0.v, ball_1.v, ball_0.pos, ball_1.pos)
        if mag(ball_0.pos - ball_2.pos) <= 2*size and dot(ball_0.pos - ball_2.pos,ball_0.v-ball_2.v) < 0:
            ball_0.v, ball_2.v = three_D_col_for02(ball_0.v, ball_2.v, ball_0.pos, ball_2.pos)
        if mag(ball_0.pos - ball_3.pos) <= 2*size and dot(ball_0.pos - ball_3.pos,ball_0.v-ball_3.v) < 0:
            ball_0.v, ball_3.v = three_D_col_for03(ball_0.v, ball_3.v, ball_0.pos, ball_3.pos)
        if mag(ball_0.pos - ball_4.pos) <= 2*size and dot(ball_0.pos - ball_4.pos,ball_0.v-ball_4.v) < 0:
            ball_0.v, ball_4.v = three_D_col_for04(ball_0.v, ball_4.v, ball_0.pos, ball_4.pos)
        if mag(ball_0.pos - ball_5.pos) <= 2*size and dot(ball_0.pos - ball_5.pos,ball_0.v-ball_5.v) < 0:
            ball_0.v, ball_5.v = three_D_col_for05(ball_0.v, ball_5.v, ball_0.pos, ball_5.pos)
        if mag(ball_0.pos - ball_6.pos) <= 2*size and dot(ball_0.pos - ball_6.pos,ball_0.v-ball_6.v) < 0:
            ball_0.v, ball_6.v = three_D_col_for06(ball_0.v, ball_6.v, ball_0.pos, ball_6.pos)
        if mag(ball_0.pos - ball_7.pos) <= 2*size and dot(ball_0.pos - ball_7.pos,ball_0.v-ball_7.v) < 0:
            ball_0.v, ball_7.v = three_D_col_for07(ball_0.v, ball_7.v, ball_0.pos, ball_7.pos)
        if mag(ball_0.pos - ball_8.pos) <= 2*size and dot(ball_0.pos - ball_8.pos,ball_0.v-ball_8.v) < 0:
            ball_0.v, ball_8.v = three_D_col_for08(ball_0.v, ball_8.v, ball_0.pos, ball_8.pos)
        if mag(ball_0.pos - ball_9.pos) <= 2*size and dot(ball_0.pos - ball_9.pos,ball_0.v-ball_9.v) < 0:
            ball_0.v, ball_9.v = three_D_col_for09(ball_0.v, ball_9.v, ball_0.pos, ball_9.pos)

        if mag(ball_1.pos - ball_2.pos) <= 2*size and dot(ball_1.pos - ball_2.pos,ball_1.v-ball_2.v) < 0:
            ball_1.v, ball_2.v = three_D_col_for12(ball_1.v, ball_2.v, ball_1.pos, ball_2.pos)
        if mag(ball_1.pos - ball_3.pos) <= 2*size and dot(ball_1.pos - ball_3.pos,ball_1.v-ball_3.v) < 0:
            ball_1.v, ball_3.v = three_D_col_for13(ball_1.v, ball_3.v, ball_1.pos, ball_3.pos)
        if mag(ball_1.pos - ball_4.pos) <= 2*size and dot(ball_1.pos - ball_4.pos,ball_1.v-ball_4.v) < 0:
            ball_1.v, ball_4.v = three_D_col_for14(ball_1.v, ball_4.v, ball_1.pos, ball_4.pos)
        if mag(ball_1.pos - ball_5.pos) <= 2*size and dot(ball_1.pos - ball_5.pos,ball_1.v-ball_5.v) < 0:
            ball_1.v, ball_5.v = three_D_col_for15(ball_1.v, ball_5.v, ball_1.pos, ball_5.pos)
        if mag(ball_1.pos - ball_6.pos) <= 2*size and dot(ball_1.pos - ball_6.pos,ball_1.v-ball_6.v) < 0:
            ball_1.v, ball_6.v = three_D_col_for16(ball_1.v, ball_6.v, ball_1.pos, ball_6.pos)
        if mag(ball_1.pos - ball_7.pos) <= 2*size and dot(ball_1.pos - ball_7.pos,ball_1.v-ball_7.v) < 0:
            ball_1.v, ball_7.v = three_D_col_for17(ball_1.v, ball_7.v, ball_1.pos, ball_7.pos)
        if mag(ball_1.pos - ball_8.pos) <= 2*size and dot(ball_1.pos - ball_8.pos,ball_1.v-ball_8.v) < 0:
            ball_1.v, ball_8.v = three_D_col_for18(ball_1.v, ball_8.v, ball_1.pos, ball_8.pos)
        if mag(ball_1.pos - ball_9.pos) <= 2*size and dot(ball_1.pos - ball_9.pos,ball_1.v-ball_9.v) < 0:
            ball_1.v, ball_9.v = three_D_col_for19(ball_1.v, ball_9.v, ball_1.pos, ball_9.pos)

        if mag(ball_2.pos - ball_3.pos) <= 2*size and dot(ball_2.pos - ball_3.pos,ball_2.v-ball_3.v) < 0:
            ball_2.v, ball_3.v = three_D_col_for23(ball_2.v, ball_3.v, ball_2.pos, ball_3.pos)
        if mag(ball_2.pos - ball_4.pos) <= 2*size and dot(ball_2.pos - ball_4.pos,ball_2.v-ball_4.v) < 0:
            ball_2.v, ball_4.v = three_D_col_for24(ball_2.v, ball_4.v, ball_2.pos, ball_4.pos)
        if mag(ball_2.pos - ball_5.pos) <= 2*size and dot(ball_2.pos - ball_5.pos,ball_2.v-ball_5.v) < 0:
            ball_2.v, ball_5.v = three_D_col_for25(ball_2.v, ball_5.v, ball_2.pos, ball_5.pos)
        if mag(ball_2.pos - ball_6.pos) <= 2*size and dot(ball_2.pos - ball_6.pos,ball_2.v-ball_6.v) < 0:
            ball_2.v, ball_6.v = three_D_col_for26(ball_2.v, ball_6.v, ball_2.pos, ball_6.pos)
        if mag(ball_2.pos - ball_7.pos) <= 2*size and dot(ball_2.pos - ball_7.pos,ball_2.v-ball_7.v) < 0:
            ball_2.v, ball_7.v = three_D_col_for27(ball_2.v, ball_7.v, ball_2.pos, ball_7.pos)
        if mag(ball_2.pos - ball_8.pos) <= 2*size and dot(ball_2.pos - ball_8.pos,ball_2.v-ball_8.v) < 0:
            ball_2.v, ball_8.v = three_D_col_for28(ball_2.v, ball_8.v, ball_2.pos, ball_8.pos)
        if mag(ball_2.pos - ball_9.pos) <= 2*size and dot(ball_2.pos - ball_9.pos,ball_2.v-ball_9.v) < 0:
            ball_2.v, ball_9.v = three_D_col_for29(ball_2.v, ball_9.v, ball_2.pos, ball_9.pos)

        if mag(ball_3.pos - ball_4.pos) <= 2*size and dot(ball_3.pos - ball_4.pos,ball_3.v-ball_4.v) < 0:
            ball_3.v, ball_4.v = three_D_col_for34(ball_3.v, ball_4.v, ball_3.pos, ball_4.pos)
        if mag(ball_3.pos - ball_5.pos) <= 2*size and dot(ball_3.pos - ball_5.pos,ball_3.v-ball_5.v) < 0:
            ball_3.v, ball_5.v = three_D_col_for35(ball_3.v, ball_5.v, ball_3.pos, ball_5.pos)        
        if mag(ball_3.pos - ball_6.pos) <= 2*size and dot(ball_3.pos - ball_6.pos,ball_3.v-ball_6.v) < 0:
            ball_3.v, ball_6.v = three_D_col_for36(ball_3.v, ball_6.v, ball_3.pos, ball_6.pos)
        if mag(ball_3.pos - ball_7.pos) <= 2*size and dot(ball_3.pos - ball_7.pos,ball_3.v-ball_7.v) < 0:
            ball_3.v, ball_7.v = three_D_col_for37(ball_3.v, ball_7.v, ball_3.pos, ball_7.pos)        
        if mag(ball_3.pos - ball_8.pos) <= 2*size and dot(ball_3.pos - ball_8.pos,ball_3.v-ball_8.v) < 0:
            ball_3.v, ball_8.v = three_D_col_for38(ball_3.v, ball_8.v, ball_3.pos, ball_8.pos)                
        if mag(ball_3.pos - ball_9.pos) <= 2*size and dot(ball_3.pos - ball_9.pos,ball_3.v-ball_9.v) < 0:
            ball_3.v, ball_9.v = three_D_col_for39(ball_3.v, ball_9.v, ball_3.pos, ball_9.pos)   

        if mag(ball_4.pos - ball_5.pos) <= 2*size and dot(ball_4.pos - ball_5.pos,ball_4.v-ball_5.v) < 0:
            ball_4.v, ball_5.v = three_D_col_for45(ball_4.v, ball_5.v, ball_4.pos, ball_5.pos)
        if mag(ball_4.pos - ball_6.pos) <= 2*size and dot(ball_4.pos - ball_6.pos,ball_4.v-ball_6.v) < 0:
            ball_4.v, ball_6.v = three_D_col_for46(ball_4.v, ball_6.v, ball_4.pos, ball_6.pos)
        if mag(ball_4.pos - ball_7.pos) <= 2*size and dot(ball_4.pos - ball_7.pos,ball_4.v-ball_7.v) < 0:
            ball_4.v, ball_7.v = three_D_col_for47(ball_4.v, ball_7.v, ball_4.pos, ball_7.pos)
        if mag(ball_4.pos - ball_8.pos) <= 2*size and dot(ball_4.pos - ball_8.pos,ball_4.v-ball_8.v) < 0:
            ball_4.v, ball_8.v = three_D_col_for48(ball_4.v, ball_8.v, ball_4.pos, ball_8.pos)
        if mag(ball_4.pos - ball_9.pos) <= 2*size and dot(ball_4.pos - ball_9.pos,ball_4.v-ball_9.v) < 0:
            ball_4.v, ball_9.v = three_D_col_for49(ball_4.v, ball_9.v, ball_4.pos, ball_9.pos)

        if mag(ball_5.pos - ball_6.pos) <= 2*size and dot(ball_5.pos - ball_6.pos,ball_5.v-ball_6.v) < 0:
            ball_5.v, ball_6.v = three_D_col_for56(ball_5.v, ball_6.v, ball_5.pos, ball_6.pos)
        if mag(ball_5.pos - ball_7.pos) <= 2*size and dot(ball_5.pos - ball_7.pos,ball_5.v-ball_7.v) < 0:
            ball_5.v, ball_7.v = three_D_col_for57(ball_5.v, ball_7.v, ball_5.pos, ball_7.pos)
        if mag(ball_5.pos - ball_8.pos) <= 2*size and dot(ball_5.pos - ball_8.pos,ball_5.v-ball_8.v) < 0:
            ball_5.v, ball_8.v = three_D_col_for58(ball_5.v, ball_8.v, ball_5.pos, ball_8.pos)
        if mag(ball_5.pos - ball_9.pos) <= 2*size and dot(ball_5.pos - ball_9.pos,ball_5.v-ball_9.v) < 0:
            ball_5.v, ball_9.v = three_D_col_for59(ball_5.v, ball_9.v, ball_5.pos, ball_9.pos)

        if mag(ball_6.pos - ball_7.pos) <= 2*size and dot(ball_6.pos - ball_7.pos,ball_6.v-ball_7.v) < 0:
            ball_6.v, ball_7.v = three_D_col_for67(ball_6.v, ball_7.v, ball_6.pos, ball_7.pos)
        if mag(ball_6.pos - ball_8.pos) <= 2*size and dot(ball_6.pos - ball_8.pos,ball_6.v-ball_8.v) < 0:
            ball_6.v, ball_8.v = three_D_col_for68(ball_6.v, ball_8.v, ball_6.pos, ball_8.pos)
        if mag(ball_6.pos - ball_9.pos) <= 2*size and dot(ball_6.pos - ball_9.pos,ball_6.v-ball_9.v) < 0:
            ball_6.v, ball_9.v = three_D_col_for69(ball_6.v, ball_9.v, ball_6.pos, ball_9.pos)

        if mag(ball_7.pos - ball_8.pos) <= 2*size and dot(ball_7.pos - ball_8.pos,ball_7.v-ball_8.v) < 0:
            ball_7.v, ball_8.v = three_D_col_for78(ball_7.v, ball_8.v, ball_7.pos, ball_8.pos)
        if mag(ball_7.pos - ball_9.pos) <= 2*size and dot(ball_7.pos - ball_9.pos,ball_7.v-ball_9.v) < 0:
            ball_7.v, ball_9.v = three_D_col_for79(ball_7.v, ball_9.v, ball_7.pos, ball_9.pos)
            
        if mag(ball_8.pos - ball_9.pos) <= 2*size and dot(ball_8.pos - ball_9.pos,ball_8.v-ball_9.v) < 0:
            ball_8.v, ball_9.v = three_D_col_for89(ball_8.v, ball_9.v, ball_8.pos, ball_9.pos)
            
        #當球入洞
        if mag(ball_0.pos - hp1) <=detnum-3.5 or mag(ball_0.pos - hp2) <=detnum-3.5 or mag(ball_0.pos - hp3) <=detnum-3.5 or mag(ball_0.pos - hp4) <=detnum-3.5 or mag(ball_0.pos - hp5) <=detnum-3.5 or mag(ball_0.pos - hp6) <=detnum-3.5:
            ball_0.v=vector(0,0,0)
            ball_0.visible = False
            ball_0.pos.y=ball_0.pos.y - 5
            print('Ball Reset')
            ball_0.pos=vec(0,size,53.5)
            ball_0.visible = True
            log.pos=ball_0.pos
            ball_0.v=vec(0,0,0)
            ball_1.v=vec(0,0,0)
            ball_2.v=vec(0,0,0)
            ball_3.v=vec(0,0,0)
            ball_4.v=vec(0,0,0)
            ball_5.v=vec(0,0,0)
            ball_6.v=vec(0,0,0)
            ball_7.v=vec(0,0,0)
            ball_8.v=vec(0,0,0)
            ball_9.v=vec(0,0,0)
            break
        if mag(ball_1.pos - hp1) <=detnum or mag(ball_1.pos - hp2) <=detnum or mag(ball_1.pos - hp3) <=detnum or mag(ball_1.pos - hp4) <=detnum or mag(ball_1.pos - hp5) <=detnum or mag(ball_1.pos - hp6) <=detnum:
            ball_1.v=vector(0,0,0)
            ball_1.visible = False
            ball_1.pos.y=ball_1.pos.y - 5
            ball1fall=1
        if mag(ball_2.pos - hp1) <=detnum or mag(ball_2.pos - hp2) <=detnum or mag(ball_2.pos - hp3) <=detnum or mag(ball_2.pos - hp4) <=detnum or mag(ball_2.pos - hp5) <=detnum or mag(ball_2.pos - hp6) <=detnum:
            ball_2.v=vector(0,0,0)
            ball_2.pos.y=ball_2.pos.y - 5
            ball_2.visible = False
            ball2fall=1
        if mag(ball_3.pos - hp1) <=detnum or mag(ball_3.pos - hp2) <=detnum or mag(ball_3.pos - hp3) <=detnum or mag(ball_3.pos - hp4) <=detnum or mag(ball_3.pos - hp5) <=detnum or mag(ball_3.pos - hp6) <=detnum:
            ball_3.v=vector(0,0,0)
            ball_3.pos.y=ball_3.pos.y - 5
            ball_3.visible = False
            ball3fall=1
        if mag(ball_4.pos - hp1) <=detnum or mag(ball_4.pos - hp2) <=detnum or mag(ball_4.pos - hp3) <=detnum or mag(ball_4.pos - hp4) <=detnum or mag(ball_4.pos - hp5) <=detnum or mag(ball_4.pos - hp6) <=detnum:
            ball_4.v=vector(0,0,0)
            ball_4.pos.y=ball_4.pos.y - 5
            ball_4.visible = False
            ball4fall=1
        if mag(ball_5.pos - hp1) <=detnum or mag(ball_5.pos - hp2) <=detnum or mag(ball_5.pos - hp3) <=detnum or mag(ball_5.pos - hp4) <=detnum or mag(ball_5.pos - hp5) <=detnum or mag(ball_5.pos - hp6) <=detnum:
            ball_5.v=vector(0,0,0)
            ball_5.pos.y=ball_5.pos.y - 5
            ball_5.visible = False
            ball5fall=1
        if mag(ball_6.pos - hp1) <=detnum or mag(ball_6.pos - hp2) <=detnum or mag(ball_6.pos - hp3) <=detnum or mag(ball_6.pos - hp4) <=detnum or mag(ball_6.pos - hp5) <=detnum or mag(ball_6.pos - hp6) <=detnum:
            ball_6.v=vector(0,0,0)
            ball_6.pos.y=ball_6.pos.y - 5
            ball_6.visible = False
            ball6fall=1
        if mag(ball_7.pos - hp1) <=detnum or mag(ball_7.pos - hp2) <=detnum or mag(ball_7.pos - hp3) <=detnum or mag(ball_7.pos - hp4) <=detnum or mag(ball_7.pos - hp5) <=detnum or mag(ball_7.pos - hp6) <=detnum:
            ball_7.v=vector(0,0,0)
            ball_7.pos.y=ball_7.pos.y - 5
            ball_7.visible = False
            ball7fall=1
        if mag(ball_8.pos - hp1) <=detnum or mag(ball_8.pos - hp2) <=detnum or mag(ball_8.pos - hp3) <=detnum or mag(ball_8.pos - hp4) <=detnum or mag(ball_8.pos - hp5) <=detnum or mag(ball_8.pos - hp6) <=detnum:
            ball_8.v=vector(0,0,0)
            ball_8.pos.y=ball_8.pos.y - 5
            ball_8.visible = False
            ball8fall=1
        if mag(ball_9.pos - hp1) <=detnum or mag(ball_9.pos - hp2) <=detnum or mag(ball_9.pos - hp3) <=detnum or mag(ball_9.pos - hp4) <=detnum or mag(ball_9.pos - hp5) <=detnum or mag(ball_9.pos - hp6) <=detnum:
            ball_9.v=vector(0,0,0)
            ball_9.pos.y=ball_9.pos.y - 5
            ball_9.visible = False
            ball9fall=1                        
        '''      
        if ball0fall==1:
            while True:
                rate(1000)
                ball_0.v=vector(0,-4.0,0)
                ball_0.pos = ball_0.pos + ball_0.v*dt
                if ball_0.pos.y <= -4:
                    ball0fall=0
                    ball_0.v=(0,0,0)
                    break
        '''

            
        #當球碰到牆壁(共9組)

        if ball_0.pos.z + size > W/2 :
            ball_0.v.z = -ball_0.v.z
        if ball_0.pos.z - size < -W/2  :
            ball_0.v.z = -ball_0.v.z
        if ball_0.pos.x + size > L/2 :
            ball_0.v.x = -ball_0.v.x
        if ball_0.pos.x - size < -L/2 :
            ball_0.v.x = -ball_0.v.x

        if ball_1.pos.z + size > W/2 :
            ball_1.v.z = -ball_1.v.z
        if ball_1.pos.z - size < -W/2  :
            ball_1.v.z = -ball_1.v.z
        if ball_1.pos.x + size > L/2 :
            ball_1.v.x = -ball_1.v.x
        if ball_1.pos.x - size < -L/2 :
            ball_1.v.x = -ball_1.v.x

        if ball_2.pos.z + size > W/2 :
            ball_2.v.z = -ball_2.v.z
        if ball_2.pos.z - size < -W/2  :
            ball_2.v.z = -ball_2.v.z
        if ball_2.pos.x + size > L/2 :
            ball_2.v.x = -ball_2.v.x
        if ball_2.pos.x - size < -L/2 :
            ball_2.v.x = -ball_2.v.x
            
        if ball_3.pos.z + size > W/2 :
            ball_3.v.z = -ball_3.v.z
        if ball_3.pos.z - size < -W/2  :
            ball_3.v.z = -ball_3.v.z
        if ball_3.pos.x + size > L/2 :
            ball_3.v.x = -ball_3.v.x
        if ball_3.pos.x - size < -L/2 :
            ball_3.v.x = -ball_3.v.x
            
        if ball_4.pos.z + size > W/2 :
            ball_4.v.z = -ball_4.v.z
        if ball_4.pos.z - size < -W/2  :
            ball_4.v.z = -ball_4.v.z
        if ball_4.pos.x + size > L/2 :
            ball_4.v.x = -ball_4.v.x
        if ball_4.pos.x - size < -L/2 :
            ball_4.v.x = -ball_4.v.x

        if ball_5.pos.z + size > W/2 :
            ball_5.v.z = -ball_5.v.z
        if ball_5.pos.z - size < -W/2  :
            ball_5.v.z = -ball_5.v.z
        if ball_5.pos.x + size > L/2 :
            ball_5.v.x = -ball_5.v.x
        if ball_5.pos.x - size < -L/2 :
            ball_5.v.x = -ball_5.v.x

        if ball_6.pos.z + size > W/2 :
            ball_6.v.z = -ball_6.v.z
        if ball_6.pos.z - size < -W/2  :
            ball_6.v.z = -ball_6.v.z
        if ball_6.pos.x + size > L/2 :
            ball_6.v.x = -ball_6.v.x
        if ball_6.pos.x - size < -L/2 :
            ball_6.v.x = -ball_6.v.x

        if ball_7.pos.z + size > W/2 :
            ball_7.v.z = -ball_7.v.z
        if ball_7.pos.z - size < -W/2  :
            ball_7.v.z = -ball_7.v.z
        if ball_7.pos.x + size > L/2 :
            ball_7.v.x = -ball_7.v.x
        if ball_7.pos.x - size < -L/2 :
            ball_7.v.x = -ball_7.v.x

        if ball_8.pos.z + size > W/2 :
            ball_8.v.z = -ball_8.v.z
        if ball_8.pos.z - size < -W/2  :
            ball_8.v.z = -ball_8.v.z
        if ball_8.pos.x + size > L/2 :
            ball_8.v.x = -ball_8.v.x
        if ball_8.pos.x - size < -L/2 :
            ball_8.v.x = -ball_8.v.x

        if ball_9.pos.z + size > W/2 :
            ball_9.v.z = -ball_9.v.z
        if ball_9.pos.z - size < -W/2  :
            ball_9.v.z = -ball_9.v.z
        if ball_9.pos.x + size > L/2 :
            ball_9.v.x = -ball_9.v.x
        if ball_9.pos.x - size < -L/2 :
            ball_9.v.x = -ball_9.v.x    

    #摩擦力

        if ball_0.v.z > 0:
            ball_0.v.z = ball_0.v.z - vN*dt
        if ball_0.v.z < 0:
            ball_0.v.z = ball_0.v.z + vN*dt
        if ball_0.v.x > 0:
            ball_0.v.x = ball_0.v.x - vN*dt
        if ball_0.v.x < 0:
            ball_0.v.x = ball_0.v.x + vN*dt

        if ball_1.v.z > 0:
            ball_1.v.z = ball_1.v.z - vN*dt
        if ball_1.v.z < 0:
            ball_1.v.z = ball_1.v.z + vN*dt
        if ball_1.v.x > 0:
            ball_1.v.x = ball_1.v.x - vN*dt
        if ball_1.v.x < 0:
            ball_1.v.x = ball_1.v.x + vN*dt

        if ball_2.v.z > 0:
            ball_2.v.z = ball_2.v.z - vN*dt
        if ball_2.v.z < 0:
            ball_2.v.z = ball_2.v.z + vN*dt
        if ball_2.v.x > 0:
            ball_2.v.x = ball_2.v.x - vN*dt
        if ball_2.v.x < 0:
            ball_2.v.x = ball_2.v.x + vN*dt

        if ball_3.v.z > 0:
            ball_3.v.z = ball_3.v.z - vN*dt
        if ball_3.v.z < 0:
            ball_3.v.z = ball_3.v.z + vN*dt
        if ball_3.v.x > 0:
            ball_3.v.x = ball_3.v.x - vN*dt
        if ball_3.v.x < 0:
            ball_3.v.x = ball_3.v.x + vN*dt

        if ball_4.v.z > 0:
            ball_4.v.z = ball_4.v.z - vN*dt
        if ball_4.v.z < 0:
            ball_4.v.z = ball_4.v.z + vN*dt
        if ball_4.v.x > 0:
            ball_4.v.x = ball_4.v.x - vN*dt
        if ball_4.v.x < 0:
            ball_4.v.x = ball_4.v.x + vN*dt

        if ball_5.v.z > 0:
            ball_5.v.z = ball_5.v.z - vN*dt
        if ball_5.v.z < 0:
            ball_5.v.z = ball_5.v.z + vN*dt
        if ball_5.v.x > 0:
            ball_5.v.x = ball_5.v.x - vN*dt
        if ball_5.v.x < 0:
            ball_5.v.x = ball_5.v.x + vN*dt

        if ball_6.v.z > 0:
            ball_6.v.z = ball_6.v.z - vN*dt
        if ball_6.v.z < 0:
            ball_6.v.z = ball_6.v.z + vN*dt
        if ball_6.v.x > 0:
            ball_6.v.x = ball_6.v.x - vN*dt
        if ball_6.v.x < 0:
            ball_6.v.x = ball_6.v.x + vN*dt

        if ball_7.v.z > 0:
            ball_7.v.z = ball_7.v.z - vN*dt
        if ball_7.v.z < 0:
            ball_7.v.z = ball_7.v.z + vN*dt
        if ball_7.v.x > 0:
            ball_7.v.x = ball_7.v.x - vN*dt
        if ball_7.v.x < 0:
            ball_7.v.x = ball_7.v.x + vN*dt

        if ball_8.v.z > 0:
            ball_8.v.z = ball_8.v.z - vN*dt
        if ball_8.v.z < 0:
            ball_8.v.z = ball_8.v.z + vN*dt
        if ball_8.v.x > 0:
            ball_8.v.x = ball_8.v.x - vN*dt
        if ball_8.v.x < 0:
            ball_8.v.x = ball_8.v.x + vN*dt

        if ball_9.v.z > 0:
            ball_9.v.z = ball_9.v.z - vN*dt
        if ball_9.v.z < 0:
            ball_9.v.z = ball_9.v.z + vN*dt
        if ball_9.v.x > 0:
            ball_9.v.x = ball_9.v.x - vN*dt
        if ball_9.v.x < 0:
            ball_9.v.x = ball_9.v.x + vN*dt

        if ball1fall==1 and ball2fall==1 and ball3fall==1 and ball4fall==1 and ball5fall==1 and ball6fall==1 and ball7fall==1 and ball8fall==1 and ball9fall==1:
            print ('End Game')
            print ('遊戲時間'+str(t/3))
        
        if ball_0.v.x <= vN*dt and ball_0.v.x>=0 or ball_0.v.x >= -vN*dt and ball_0.v.x<=0:
            det0=1    
        if ball_1.v.x <= vN*dt and ball_1.v.x>=0 or ball_1.v.x >= -vN*dt and ball_1.v.x<=0:
            det1=1     
        if ball_2.v.x <= vN*dt and ball_2.v.x>=0 or ball_2.v.x >= -vN*dt and ball_2.v.x<=0:
            det2=1
        if ball_3.v.x <=vN*dt and ball_3.v.x>=0 or ball_3.v.x >= -vN*dt and ball_3.v.x<=0:
            det3=1
        if ball_4.v.x <=vN*dt and ball_4.v.x>=0 or ball_4.v.x >= -vN*dt and ball_4.v.x<=0:
            det4=1
        if ball_5.v.x <=vN*dt and ball_5.v.x>=0 or ball_5.v.x >= -vN*dt and ball_5.v.x<=0:
            det5=1
        if ball_6.v.x <=vN*dt and ball_6.v.x>=0 or ball_6.v.x >= -vN*dt and ball_6.v.x<=0:
            det6=1
        if ball_7.v.x <=vN*dt and ball_7.v.x>=0 or ball_7.v.x >= -vN*dt and ball_7.v.x<=0:
            det7=1
        if ball_8.v.x <=vN*dt and ball_8.v.x>=0 or ball_8.v.x >= -vN*dt and ball_8.v.x<=0:
            det8=1
        if ball_9.v.x <=vN*dt and ball_9.v.x>=0 or ball_9.v.x >= -vN*dt and ball_9.v.x<=0:
            det9=1                                    
        if det0==1 and det1==1 and det2==1 and det3==1 and det4==1 and det5==1 and det6==1 and det7==1 and det8==1 and det9==1:
            det0=det1=det2=det3=det4=det5=det6=det7=det8=det9=0
            ball_0.v=vector(0,0,0)
            ball_1.v=vector(0,0,0)
            ball_2.v=vector(0,0,0)
            ball_3.v=vector(0,0,0)
            ball_4.v=vector(0,0,0)
            ball_5.v=vector(0,0,0)
            ball_6.v=vector(0,0,0)
            ball_7.v=vector(0,0,0)
            ball_8.v=vector(0,0,0)
            ball_9.v=vector(0,0,0)
            log.pos=ball_0.pos
            break
        
    while True:
        rate(1000)
        m_ev = scene.waitfor('click mousedown mouseup mousemove')  #滑鼠event
        
        if m_ev.event == 'mousedown':  #如果滑鼠按下左鍵
            if mag(ball_0.pos-m_ev.pos) <= by: #若滑鼠位置與尾端的位置差小於by
                ball_0.v.z = -(log.axis.z - ball_0.pos.z)*2.5
                ball_0.v.x = -(log.axis.x - ball_0.pos.x)*2.5
                log.visible = False
                break
        else:
            log.visible = True
            log.axis.x=m_ev.pos.x-ball_0.pos.x
            log.axis.z=m_ev.pos.z-ball_0.pos.z


  #  while True:        
        

           
'''
    if drag: #如果滑鼠正在按下拖曳tail or tip)
        #new_pos = m_ev.pos #把目前滑鼠的位置紀錄於new_pos
        if drag == 'click':
            ball_0.v.z = (ball_0.pos.z - m_ev.pos.z)*5000
            ball_0.v.x = (ball_0.pos.x - m_ev.pos.x)*5000
'''
#可能要複製到單機版才能正常運行
