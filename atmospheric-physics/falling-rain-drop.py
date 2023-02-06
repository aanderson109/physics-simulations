import vpython 

# setting the scene
scene.width=500 # "meters"
scene.height=500  # "meters"
scene.background=vec(47/255, 141/255, 255/255)
scene.center=vec(0, 250, 0)

# the ground
ground=box(pos=vec(0,-10,0), size=vec(500, 10, 1),
  color=vec(86/255, 125/255, 70/255))

# the raindrop
drop=sphere(pos=vec(0, 500, 0), radius=8, vel=vec(0 ,0, 0),
  color=color.blue)

# the cloud
for x in range(-250,250,6.5):
  for y in range(500,550,6.5):
    cloud=sphere(pos=vec(x, y, -20), radius=25*random(),
    color=color.gray(0.9))

# constants, parameters & such
dt=0.1  # time step ~ sec
t=0     # initial time ~ sec
g=9.8   # gravitational acceleration ~ m/s^2
a=vec(0,-g,0)   # acceleration vector ~ m/s^2
Rdrop=2e-5      # radius of raindrop ~ meters (20 micrometers)
u=1.8e-5        #viscosity of air ~ Pa*sec
k=6*pi*Rdrop*u  #drag force constant ~ N*sec/meter
rhoWater=1000   #density of water ~ kg/m^3
VLdrop=(4/3)*pi*(Rdrop**3)    #volume of raindrop ~ meters^3
Mdrop=rhoWater*VLdrop         # mass of the drop ~ kg
vt=(Mdrop*a)/k  # terminal velocity of drop  ~ m/sec
km=k/Mdrop      # constant k divided by drop mass ~ 1/sec

# weight & drag force arrows
Fgarr=arrow(pos=drop.pos, axis=a.hat, length=(Mdrop*g)*(1e11),
  color=color.red, shaftwidth=5)
Fdarr=arrow(pos=drop.pos, axis=-a.hat, length=1,
  color=color.red, shaftwidth=5)

# graph of drop's velocity vs time
graphv=graph(width=500, title='<b>velocity (m/s) vs. time (s)</b>', xtitle='t(s)',
  ytitle='v(m/s)', foreground=color.black, background=color.white)
v1=gcurve(graph=graphv, color=color.red)

scene.waitfor('click')  # wait for mouse click before starting

# while loop to animate this bad boy
while t<2*6000:
  rate(10000) #rate of iterations animated
  drop.vel=vt + (drop.vel - vt)*exp((-km)*dt)
  drop.pos=drop.pos + drop.vel*dt + (1/2)*a*(dt**2)   # kinematic equation of the drop
  Fdrag=k*drop.vel.mag  #calculates small drop drag force as it changes w/ time
  Fdarr.length=Fdrag*(1e11)
  Fgarr.pos=drop.pos   # moves weight force arrow with drop
  Fdarr.pos=drop.pos   # moves drag force arrow with drop
  print(t, "s", "\t", drop.vel.mag, "m/s", "\t", Fdrag, "N")  # prints time & velocity w/ units
  v1.plot(t, drop.vel.mag)  # plots magnitude of drops velocity w.r.t time
  t=t+dt
  if drop.pos.y<=0:  # if/else statement to end things when drop reaches ground
    print("Rain drop reached the ground!!")
    print("Total Time Taken: ", t, "s", " or", t/60, "minutes",
    "\nTerminal Velocity: ", drop.vel.mag, " m/s")
    break
