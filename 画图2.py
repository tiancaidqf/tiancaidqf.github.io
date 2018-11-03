import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-3, 3, 500)
x1 = np.e**t
x2 = np.e**-t
x3 = np.e**0*t
plt.figure()
plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x3)
ax = plt.gca() 
plt.xticks([])
plt.yticks([])                                          
ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')        
ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.set_title("x(t)=Ce^st")
plt.show()

