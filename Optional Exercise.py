import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

k=0.5
phi=0.66667
A=1.5

theta=0.2
omega=0.0
t=0.0
dt=0.01
dt=2*np.pi/(1000.0*phi)


iteration_number=0
transient=5000

#f(theta,omega,t)
def f(a,b,c):
    result=-np.sin(a)-k*b+A*np.cos(phi*c)
    return result

t=0.0
maxsteps=200000
thetaarray=np.zeros(maxsteps)
omegaarray=np.zeros(maxsteps)
thetaarray[0]=3.0
omegaarray[0]=0.0
i=0
while i<maxsteps-1:
    k1a=dt*omegaarray[i]
    k1b=dt*f(thetaarray[i], omegaarray[i], t)
    k2a=dt*(omegaarray[i]+k1b/2)
    k2b=dt*f(thetaarray[i]+k1a/2,omegaarray[i]+k1b/2,t+dt/2)
    k3a=dt*(omegaarray[i]+k2b/2)
    k3b=dt*f(thetaarray[i]+k2a/2,omegaarray[i]+k2b/2,t+dt/2)
    k4a=dt*(omegaarray[i]+k3b)
    k4b=dt*f(thetaarray[i]+k3a,omegaarray[i]+k3b,t+dt)
    thetaarray[i+1]=thetaarray[i]+(k1a+2*k2a+2*k3a+k4a)/6
    omegaarray[i+1]=omegaarray[i]+(k1b+2*k2b+2*k3b+k4b)/6
    iteration_number=iteration_number+1
    if (np.abs(thetaarray[i+1])>np.pi):
        thetaarray[i+1]-=2*np.pi*np.abs(thetaarray[i+1])/thetaarray[i+1]
    t=t+dt
    i=i+1

pickedtheta=[]
pickedomega=[]
i=1
while i<int(maxsteps/1000):
    pickedtheta.append(thetaarray[1000*i])
    pickedomega.append(omegaarray[1000*i])
    i=i+1
plt.scatter(pickedtheta,pickedomega,s=2)


