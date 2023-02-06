import scipy
from pylab import *
from scipy.integrate import odeint

N = 1000
L_o = 1.0  #unstretched spring length
L = 1.0    # Initial stretch of spring
v_o = 0.0  # initial velocity
theta_o = 0.3  #radians
omega_o = 0.0  # initial angular velocity
y = zeros([4])

y[0] = L
y[1] = v_o
y[2] = theta_o
y[3] = omega_o

time = np.linspace(0, 25, N)
k = 3.5
m = 0.2
grav = 9.8

def spring_pendulum(y, time):
    g0 = y[1]
    g1 = (L_o + y[0])*y[3] - k/m*y[0] + grav*np.cos(y[2])
    g2 = y[3]
    g3 = -(grav*np.sin(y[2]) + 2.0*y[1]*y[3])/(L_o + y[0])
    
    return np.array([g0, g1, g2, g3])
answer = scipy.integrate.odeint(spring_pendulum, y, time)
xdata = (L_o + answer[:,0])*np.sin(answer[:,2])
ydata = -(L_o + answer[:,0])*np.cos(answer[:,2])

plt.plot(xdata,ydata, 'r-')
plt.xlabel('Horizontal Position')
plt.ylabel('Vertical Position')
plt.show()
