import numpy as np
import matplotlib.pyplot as plt

k=0.5
phi=0.66667
A=0.0

theta=0.2
omega=0.0
t=0.0
dt=0.01

#f(theta,omega,t)
def f(a,b,c):
    result=-np.sin(a)-k*b+A*np.cos(phi*c)
    return result

t=0.0
maxsteps=3000
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
    t=t+dt
    i=i+1
time=np.linspace(0,t,maxsteps)
plt.scatter(time,omegaarray,s=0.1,c=time,cmap='autumn')
plt.xlim(0,t)
plt.xlabel(r'$t$')
span1=max(omegaarray)-min(omegaarray)
plt.ylim(min(omegaarray)-0.1*span1,max(omegaarray)+0.1*span1)
plt.ylabel(r'$\omega(t)$')
plt.title(r'$\omega(t)$ vs $t$ ($\theta=3.0$, $\omega=0.0$)')
plt.savefig('Ex4/1.4.pdf')
plt.show()

plt.scatter(time,thetaarray,s=0.1,c=time,cmap='winter')
plt.xlim(0,t)
plt.xlabel(r'$t$')
span2=max(thetaarray)-min(thetaarray)
plt.ylim(min(thetaarray)-0.1*span2,max(thetaarray)+0.1*span2)
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=3.0$, $\omega=0.0$)')
plt.savefig('Ex4/2.4.pdf')
plt.show()