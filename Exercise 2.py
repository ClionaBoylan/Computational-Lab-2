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
maxsteps=6000
thetaarray=np.zeros(maxsteps)
omegaarray=np.zeros(maxsteps)
thetaarray[0]=0.2
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
plt.scatter(time,omegaarray,s=0.1,c=time,cmap='autumn')
plt.scatter(time,thetaarray,s=0.1,c=time,cmap='winter')
plt.xlim(0,t)
plt.ylim(-1.0,1.0)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=0.2$, $\omega=0.0$)')
plt.savefig('Ex2/1.1.pdf')
plt.show()

t=0.0
thetaarray=np.zeros(maxsteps)
omegaarray=np.zeros(maxsteps)
thetaarray[0]=1.0
omegaarray[0]=0.0
i=0
while i<maxsteps-1:
    k1a=dt*omegaarray[i]
    k1b=dt*f(thetaarray[i], omegaarray[i], t)
    k2a=dt*(omegaarray[i]+k1b)
    k2b=dt*f(thetaarray[i]+k1a,omegaarray[i]+k1b,t+dt)
    thetaarray[i+1]=thetaarray[i]+(k1a+k2a)/2
    omegaarray[i+1]=omegaarray[i]+(k1b+k2b )/2
    t=t+dt
    i=i+1
time=np.linspace(0,t,maxsteps)
plt.scatter(time,omegaarray,s=0.1,c=time,cmap='autumn')
plt.scatter(time,thetaarray,s=0.1,c=time,cmap='winter')
plt.xlim(0,t)
plt.ylim(-1.5,1.5)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=1.0$, $\omega=0.0$)')
plt.savefig('Ex2/2.1.pdf')
plt.show()

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
    
plt.scatter(time,omegaarray,s=0.1,c=time,cmap='autumn')
plt.scatter(time,thetaarray,s=0.1,c=time,cmap='winter')
plt.xlim(0,t)
#plt.ylim(-np.pi-0.1,np.pi+0.1)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=3.14$, $\omega=0.0$)')
plt.savefig('Ex2/3.1.pdf')
plt.show()

t=0.0
thetaarray=np.zeros(maxsteps)
omegaarray=np.zeros(maxsteps)
thetaarray[0]=0.0
omegaarray[0]=1.0
i=0
while i<maxsteps-1:
    k1a=dt*omegaarray[i]
    k1b=dt*f(thetaarray[i], omegaarray[i], t)
    k2a=dt*(omegaarray[i]+k1b)
    k2b=dt*f(thetaarray[i]+k1a,omegaarray[i]+k1b,t+dt)
    thetaarray[i+1]=thetaarray[i]+(k1a+k2a)/2
    omegaarray[i+1]=omegaarray[i]+(k1b+k2b )/2
    t=t+dt
    i=i+1
time=np.linspace(0,t,maxsteps)
plt.scatter(time,omegaarray,s=0.1,c=time,cmap='autumn')
plt.scatter(time,thetaarray,s=0.1,c=time,cmap='winter')
plt.xlim(0,t)
plt.ylim(-np.pi,np.pi)
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta(t)$')
plt.title(r'$\theta(t)$ vs $t$ ($\theta=0.0$, $\omega=1.0$)')
plt.savefig('Ex2/4.1.pdf')
plt.show()