import numpy as np
import sympy as sp
from sympy.utilities import lambdify
from sympy.solvers import solve
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation
from matplotlib.animation import PillowWriter
from IPython.display import HTML
plt.style.use('seaborn-v0_8')

class Pendulum:
    def __init__(self, l, t, theta0, v0):
        self.l = l
        self.t = t
        self.theta0 = theta0
        self.conditions = [theta0, v0]

    def solve_pendulum_motion(self):
        m, g, l, t = sp.symbols(('m', 'g', 'l', 't'))
        theta = sp.Function('theta')(t)
        dtheta = theta.diff(t)
        ddtheta = dtheta.diff(t)

        x, y  = l*sp.sin(theta), -l*sp.cos(theta)

        #kinetic energy
        T = sp.Rational(1,2)*m*(x.diff(t)**2 + y.diff(t)**2)
        #potential energy
        V = m*g*y
        #Lanragian Mechanics
        L = T - V

        #left hand side
        lhs = L.diff(theta)
        #right hand side
        rhs = sp.diff(L.diff(dtheta), t)

        eq = rhs - lhs

        eq = sp.solve(eq, ddtheta)[0]

        dthetadt_num = sp.lambdify(dtheta, dtheta)
        dudt_num = sp.lambdify((g, l, theta), eq)

        x_num, y_num = sp.lambdify((l, theta), x), sp.lambdify((l, theta), y)

        del m, g, l, t 

        g = 9.81
        l = self.l
        t = self.t
        conditions = self.conditions

        def dXdt(X, t, g, l):
            theta_num, u_num  = X

            return [dthetadt_num(u_num),
            dudt_num(g, l, theta_num)]
        
        sol = odeint(dXdt, t=t, y0=conditions, args = (g, l))
        angle = sol.T[0]
        velocity = sol.T[1]

        return x_num(l, angle), y_num(l,angle)

t = np.linspace(0, 10, 500)
pen = Pendulum(1, t, np.pi/4, 0)
x, y = pen.solve_pendulum_motion()


# plt.plot(t, x)
# plt.show()

#configuration of pendulum
x0, y0 = x[0], y[0]

fig = plt.figure()
ax = fig.add_subplot(aspect='equal')

line = ax.plot([0, x0], [0, y0], lw=3, c='green')
bob_radius = 0.08
circle = ax.add_patch(plt.Circle((x0,y0), bob_radius, fc='r', zorder=3))
ax.set_xlim([-x.max()-0.5, x.max()+0.5])
ax.set_ylim([y.min()-0.5,0.5])

#the function to animate
def animate(i):
    line.set_data([0, x[i]], [0, y[i]])
    circle.set_center((x[i], y[i]))

nsteps = len(x)
nframes = nsteps
dt = t[1] - t[0]
interval = dt*1000
ani = animation.FuncAnimation(fig, animate, frames=nframes, repeat=True, interval=interval)


HTML(ani.to_html5_video())
