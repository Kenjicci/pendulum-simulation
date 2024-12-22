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
        print(theta)
    
t = np.linspace(0, 10, 500)
pend = Pendulum(1, t, np.pi/4, 0)
pend.solve_pendulum_motion()
