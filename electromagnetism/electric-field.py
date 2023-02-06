import vpython 

GlowScript 2.7 VPython
#sphere at origin for reference
sphere(pos=vec(0,0,0), size=0.5*vec(1,1,1), color=color.blue)

#axes
x_axis=arrow(pos=vec(-10,0,0), axis=vec(20,0,0), shaftwidth=0.2, color=color.blue)
y_axis=arrow(pos=vec(0,-10,0), axis=vec(0,20,0), shaftwidth=0.2, color=color.blue)

#constants & charge
q=3.5*10**(-9)  #Coulombs
k=8.99*10**(9)  #Newton Meter Squared per Coulomb Squared
y1=2.0  #Meters
y2=-2.0 #Meters
x3=2.0  #Meters
x4=-2.0 #Meters

for xf in range(-10, 10, 10/21):
  for yf in range(-10,10, 10/21):
    Etotal=vec(0,0,0)
    for xc in range(-2, 2, 10/21):
      r1=vec(xf-xc, yf-y1, 0)
      r1mag=r1.mag
      E1=(k*q*r1)/(r1mag)**3
      
      r2=vec(xf-xc, yf-y2, 0)
      r2mag=r2.mag
      E2=(k*q*r2)/(r2mag)**3
    for yc in range(-2, 2, 16/30):
      r3=vec(xf-x3, yf-yc, 0)
      r3mag=r3.mag
      E3=(k*q*r3)/(r3mag)**3
      
      r4=vec(xf-x4, yf-yc, 0)
      r4mag=r4.mag
      E4=(k*q*r4)/(r4mag)**3
      
      Etotal=Etotal+E1+E2+E3+E4
    Ebox=Etotal.hat
    #to see Electric Field lines instead of unit vectors, make axis=Etotal
    Efield=arrow(pos=vec(xf,yf,0), axis=Ebox,
      shaftwidth=0.1, color=color.green)
