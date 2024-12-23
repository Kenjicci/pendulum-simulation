# Pendulum Simulation  

## Description
<p>This simulation models the motion of a pendulum based on Lagrangian mechanics. The system is solved using symbolic computation with the SymPy library, and the pendulum's motion is visualized using Pygame. The pendulum's position is calculated over time using the equations derived from the Lagrangian formulation, and the animation represents its swinging motion in 2D space.</p>

<br>

## Dependencies  
- Python 3.x  
- Matplotlib  
- Pygame  
- Sympy  

## How to run it?

1. Install the necessary dependencies using `pip`:

    ```bash
    pip install matplotlib pygame sympy
    ```

2. Download or clone the repository.

3. Ensure that you have Python 3.x installed on your machine.

4. Run the Python script:

    ```bash
    python pendulum.py
    ```

   This will generate a graphical window showing the pendulum's motion. The pendulum's movement is based on the initial conditions defined in the code, and you can adjust the parameters such as length, initial angle, and initial velocity to see how they affect the motion.

## Code Explanation

1. **Pendulum Class**:
   - The `Pendulum` class is responsible for defining the physical properties of the pendulum, such as its length and initial conditions (angle and velocity).
   - The `solve_pendulum_motion` method uses symbolic computation (SymPy) to derive the equations of motion from the Lagrangian, then numerically solves these equations using the `odeint` method from SciPy.

2. **Animation**:
   - The motion is visualized using Pygame, where the pendulum is drawn as a line and a circle (the bob).
   - The animation is updated frame-by-frame, showing how the pendulum moves based on the computed positions at each time step.

3. **Adjusting Parameters**:
   - You can change the initial angle, initial velocity, and pendulum length to see how they affect the motion.

## Example

- The script runs a simulation with the following default parameters:
    - Length: 1 meter
    - Initial Angle: 45 degrees
    - Initial Velocity: 0 m/s

   You can modify these parameters within the code for different behaviors.

