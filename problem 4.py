import math
from math import sqrt
from math import sin
from math import cos
from math import pi
import matplotlib.pyplot as plt 
import numpy as np 
from math import*

h = float(input("Enter the initial height of the projectile in meters: "))
v = float(input("Enter the magnitude of the velocity in m/s: "))
a = float(input("Input the angle in degrees with respect to the positive x axis at which the projectile is fired: "))
ax = float(input("x-component acelleration in m/s^2: "))
ay = float(input("y-component acceleration in m/s^2: "))

if ay==0:
    print("Invalid value for y-component acceleration." )

vy = (v)*(math.sin(math.radians(a)))
vx = (v)*(math.cos(math.radians(a)))
g = 9.806

t = ((vy) + (sqrt(((vy)**2)+(2*g*h))))/(g)
rmax = (vx*t)
yy = (vy)**2/(2*g)
hmax = h + yy

tb = np.linspace(0,t,100)

xa = (vx*tb)
ya = ((h)+(vy*tb)-((9.806*(tb**2))/(2)))

tt = np.linspace(0,t,100)

x = ((vx*tt)+((1/2)*(ax)*(tt**2)))
y = ((h)+(vy*tt)+((ay*(tt**2))/(2)))

xa = (vx*tt)
ya = ((h)+(vy*tt)-((9.806*(tt**2))/(2)))

plt.plot (x,y)
plt.plot (xa,ya)
plt.xlabel('Horizontal displacement')
plt.ylabel('Vertical displacement')
plt.title('Trajectory')
plt.show()
print("Legend")
print("Orange: no air resistance10")
print("Blue: with air resistance" )
if ay==0:
    print("Invalid value for y-component acceleration." )
    