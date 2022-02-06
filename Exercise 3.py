import numpy as np
import matplotlib.pyplot as plt

k=0.0
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
maxsteps=10000
thetaarray1=np.zeros(maxsteps)
omegaarray1=np.zeros(maxsteps)
thetaarray1[0]=3.14
omegaarray1[0]=0.0
i=0
while i<maxsteps-1:
    k1a=dt*omegaarray1[i]
    k1b=dt*f(thetaarray1[i], omegaarray1[i], t)
    k2a=dt*(omegaarray1[i]+k1b/2)
    k2b=dt*f(thetaarray1[i]+k1a/2,omegaarray1[i]+k1b/2,t+dt/2)
    k3a=dt*(omegaarray1[i]+k2b/2)
    k3b=dt*f(thetaarray1[i]+k2a/2,omegaarray1[i]+k2b/2,t+dt/2)
    k4a=dt*(omegaarray1[i]+k3b)
    k4b=dt*f(thetaarray1[i]+k3a,omegaarray1[i]+k3b,t+dt)
    thetaarray1[i+1]=thetaarray1[i]+(k1a+2*k2a+2*k3a+k4a)/6
    omegaarray1[i+1]=omegaarray1[i]+(k1b+2*k2b+2*k3b+k4b)/6
    t=t+dt
    i=i+1
time=np.linspace(0,t,maxsteps)

t=0.0
thetaarray=np.zeros(maxsteps)
omegaarray=np.zeros(maxsteps)
thetaarray[0]=3.14
omegaarray[0]=0.0
i=0
while i<maxsteps-1:
    k1a=dt*omegaarray[i]
    k1b=dt*f(thetaarray[i], omegaarray[i], t)
    k2a=dt*(omegaarray[i]+k1b)
    k2b=dt*f(thetaarray[i]+k1a,omegaarray[i]+k1b,t+dt)
    thetaarray[i+1]=thetaarray[i]+(k1a+k2a)/2
    omegaarray[i+1]=omegaarray[i]+(k1b+k2b)/2
    t=t+dt
    i=i+1
time=np.linspace(0,t,maxsteps)

plt.plot(time,thetaarray, color='OrangeRed',linewidth=2.5,label='Trapezoid Rule')
plt.plot(time,thetaarray1,color='RoyalBlue',linewidth=2.5,label='Runge-Kutta Algorithm')
plt.xlim(0,t)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=3.14$, $\omega=0.0$)')
plt.legend()
plt.savefig('Ex3/1.3.pdf')
plt.show()