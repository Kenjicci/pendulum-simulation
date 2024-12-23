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

        return sol

t = np.linspace(0, 10, 500)
pen = Pendulum(1, t, np.pi/4, 0)
sol = pen.solve_pendulum_motion()

theta = sol[:, 0]
velocity = sol[:, 1]

plt.plot(t, theta, label = 'angle')
plt.plot(t, velocity, label='velocity')
plt.legend()
plt.show()