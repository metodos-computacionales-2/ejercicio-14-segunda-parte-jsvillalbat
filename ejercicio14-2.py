#!/usr/bin/env python
# coding: utf-8

# In[49]:


import matplotlib.pyplot as plt
import numpy as np


# In[50]:


euler = np.loadtxt('euler.dat')
rk4 = np.loadtxt('rk4.dat')
rk4f = np.loadtxt('rk4f.dat')


# In[51]:
# Datos de RK4 y Euler sin friccion
teuler = euler[:,0]
y0euler = euler[:,1]
y1euler = euler[:,2]

trk4 = rk4[:,0]
y0rk4 = rk4[:,1]
y1rk4 = rk4[:,2]

#Datos de Euler y RK4 con friccion
trk4f = rk4f[:,0]
y0rk4f = rk4f[:,1]
y1rk4f = rk4f[:,2]

# In[52]:

plt.figure(figsize=(12,10))

plt.subplot(2,2,1)
plt.plot(teuler,y0euler)
plt.title('Metodo de Euler y0 VS time')
plt.xlabel('time')
plt.ylabel('y0')
		  
plt.subplot(2,2,2)
plt.plot(y0euler,y1euler,label = 'Euler')
plt.plot(y0rk4,y1rk4,label = 'RK4')
plt.title('Euler vs RK4')
plt.xlabel('y0')
plt.ylabel('y1')
plt.legend()
		  
plt.subplot(2,2,4)
plt.plot(y0rk4f,y1rk4f)
plt.title('RK4 con friccion de 0.7')
plt.xlabel('y0')
plt.ylabel('y1')

plt.subplot(2,2,3)
plt.plot(trk4f,y0rk4f)
plt.title('y0 Vs time con friccion 0.7')
plt.xlabel('time')
plt.ylabel('y0')

plt.savefig('ejercicio14-2.png')






# In[ ]:




