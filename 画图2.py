import numpy as np
import matplotlib.pyplot as plt
def u(t):
    if t>=0
    return 
x=np.linspace(-np.pi,np.pi,100)
ω=np.pi
t0=np.pi
 x1(t)=sin(ωt)u(t)
 x2(t)=sin(ω(t-t0))
 x3(t)=sin(ωt)u(t-t0)
 x4(t)=sin(ω(t-t0))u(t-t0)
plt.figure(num=1)
ax = plt.gca()                                           
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')        
ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.set_title("x1(t)=sin(ωt)u(t)")
plt.show


