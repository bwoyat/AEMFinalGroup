import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Constants
MU = 3.986e14          # Earth's gravitational parameter (m^3/s^2)
R_EARTH = 6.371e6      # Earth radius (m)
ALTITUDE_LEO = 400e3   # LEO altitude (m)

def compute_acceleration(position):
    """
    Parameters:
        position: [x, y] in meters
    Returns:
        [a_x, a_y] in m/s^2, represented by numpy array
    """
    G = 6.67430e-11  # gravitational constant, m^3 kg^-1 s^-2
    M = 5.972e24     # mass of Earth, kg

    r_vec = np.array(position)
    r = np.linalg.norm(r_vec)

    # Avoid division by zero
    if r == 0:
        raise ValueError("Position vector cannot be zero.")

    # Newton's law of gravitation: a = -GM/r^3 * r_vec
    acceleration = - (G * M / r**3) * r_vec

    return acceleration

compute_acceleration([100,200])