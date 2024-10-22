"""
    建國中學 Vpython物理模擬
    作者: 物理科 賴奕帆老師
    日期: 107/08/25
    特色課程 Lecture 09 List的練習
    Practice dipole field.py
"""
from vpython import *  #引用視覺畫套件Vpython

ec = 1.6e-19  # electron charge
scene = canvas(width=1000, height=600, background=vec(0.0,0.0,0.0),range = 2e-13)
scene.title="Electric Field Vectors"
charges = [ sphere( pos = vec(-1e-13,0,0), Q = +ec, color=color.red, radius = 6e-15 ),
            sphere( pos = vec(1e-13,0,0), Q = -ec, color=color.blue, radius = 6e-15 ),         ]
def getfield(p):
    f = vector(0,0,0)
    for c in charges:
        f = f + (p-c.pos) * 8.988e9 * c.Q / mag(p-c.pos)**3
    return f

while True:
    rate(30) #以每1/30秒的週期執行下列指令
    m_ev = scene.waitfor('click mousedown mouseup mousemove')  #滑鼠event
    if m_ev.event == 'mousedown':  #如果滑鼠按下左鍵
    
        f = getfield(m_ev.pos)
        m = mag(f)
        red = max( 1-1e17/m, 0 )
        blue = min(   1e17/m, 1 )
        if red >= blue:
            blue = blue/red
            red = 1.0
        else:
            red = red/blue
            blue = 1.0
        arrow( pos=m_ev.pos, axis=f * (4e-14/1e17),
               shaftwidth = 6e-15,color=vec(red,0,blue))
