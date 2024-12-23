import numpy as np
import sympy as sp
from scipy.integrate import odeint
import pygame

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

        # Kinetic energy
        T = sp.Rational(1,2)*m*(x.diff(t)**2 + y.diff(t)**2)
        # Potential energy
        V = m*g*y
        # Lagrangian Mechanics
        L = T - V

        # Left-hand side
        lhs = L.diff(theta)
        # Right-hand side
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
        
        sol = odeint(dXdt, t=t, y0=conditions, args=(g, l))
        angle = sol.T[0]
        velocity = sol.T[1]

        return x_num(l, angle), y_num(l, angle)

t = np.linspace(0, 10, 500)
pen = Pendulum(1, t, np.pi/4, 0)
x, y = pen.solve_pendulum_motion()

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pendulum Animation')

x0, y0 = x[0], y[0]
center = (width // 2, height // 2)
bob_radius = 10

clock = pygame.time.Clock()
running = True
frame = 0
nframes = len(x)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))


    bob_pos = (int(center[0] + x[frame] * 100), int(center[1] - y[frame] * 100))  


    pygame.draw.line(screen, (0, 255, 0), center, bob_pos, 3)
    pygame.draw.circle(screen, (255, 0, 0), bob_pos, bob_radius)


    pygame.display.flip()


    frame = (frame + 1) % nframes


    clock.tick(60)


pygame.quit()
