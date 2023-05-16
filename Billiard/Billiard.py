import random
import math
import numpy as np


def simulate_billiard(num_reflections):
    """
    Simulate a particle moving inside a unit circle for num_steps steps,
    starting from a random initial position and momentum.
    """
    # Initialize the particle's position and momentum
    # Initialize particle
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    px, py = random.uniform(-1, 1), random.uniform(-1, 1)
    mag_p = math.sqrt(px ** 2 + py ** 2)
    px, py = px / mag_p, py / mag_p  # normalize momentum

    # Array to store reflection points
    reflection_points = np.zeros((num_reflections, 2))

    # Simulate the particle's motion
    for i in range(num_reflections):
        # Calculate next intersection point
        a = px ** 2 + py ** 2
        b = 2 * x * px + 2 * y * py
        c = x ** 2 + y ** 2 - 1
        t1 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        t2 = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        t = t1 if t1 > 0 else t2
        x_new = x + t * px
        y_new = y + t * py

        # Save reflection point
        reflection_points[i] = [x_new, y_new]

        # Calculate new momentum
        nx = x_new
        ny = y_new
        px = (ny ** 2 - nx ** 2) * px - 2 * nx * ny * py
        py = -2 * nx * ny * px + (nx ** 2 - ny ** 2) * py
        p_norm = np.sqrt(px ** 2 + py ** 2)
        px /= p_norm
        py /= p_norm

        # Update position
        x = x_new
        y = y_new

    return reflection_points


# def reverse_particle(px, py, x, y):
#     # Reverse particle momentum and simulate n reflections
#     x_rev, y_rev = x, y
#     px_rev, py_rev = -px, -py
#     for i in range(num_reflections):
#         # Calculate next intersection point
#         a = px_rev ** 2 + py_rev ** 2
#         b = 2 * x_rev * px_rev + 2 * y_rev * py_rev
#         c = x_rev ** 2 + y_rev ** 2 - 1
#         t1, t2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#         t = t1 if t1 > 0 else t2
#         x_rev += t * px_rev
#         y_rev += t * py_rev
#
#         # Compare to reflection point
#         if abs(x_rev - reflection_points[num_reflections - 1 - i][0]) > delta or abs(
#                 y_rev - reflection_points[num_reflections - 1 - i][1]) > delta:
#             return i + 1  # return number of reflections before deviation
#
#         # Reflect particle
#         xp_rev = px_rev * (x_rev ** 2 - y_rev ** 2) - 2 * x_rev * y_rev * py_rev
#         yp_rev = py_rev * (y_rev ** 2 - x_rev ** 2) - 2 * x_rev * y_rev * px_rev
#         px_rev, py_rev = xp_rev, yp_rev

# Define the function to calculate the new momentum after reflection
def reflect(p, n):
    # p: incident momentum, n: normal to the surface of reflection
    return p - 2 * np.dot(p, n) * n


# Define the function to simulate the billiard model
def simulate(n, delta):
    # n: number of reflections to simulate, delta: deviation threshold to test reversibility
    # Initialize the initial position and momentum of the particle
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    px, py = random.uniform(-1, 1), random.uniform(-1, 1)
    mag_p = math.sqrt(px ** 2 + py ** 2)
    px, py = px / mag_p, py / mag_p  # normalize momentum

    # Array to store reflection points
    reflection_points = np.zeros((num_reflections, 2))

    # Simulate the particle's motion
    for i in range(num_reflections):
        # Calculate next intersection point
        a = px ** 2 + py ** 2
        b = 2 * x * px + 2 * y * py
        c = x ** 2 + y ** 2 - 1
        t1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
        t2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
        t = t1 if t1 > 0 else t2
        x_new = x + t * px
        y_new = y + t * py

        # Save reflection point
        reflection_points[i] = [x_new, y_new]

        # Calculate new momentum
        nx = x_new
        ny = y_new
        px = (ny ** 2 - nx ** 2) * px - 2 * nx * ny * py
        py = -2 * nx * ny * px + (nx ** 2 - ny ** 2) * py
        p_norm = np.sqrt(px ** 2 + py ** 2)
        px /= p_norm
        py /= p_norm

        # Update position
        x = x_new
        y = y_new

        # Calculate the normal to the surface of reflection
        n = np.array([nx, ny])
        n = n / np.linalg.norm(n)

    # # Simulate the reflections
    # for i in range(n):
    #     # Calculate the intersection point with the boundary of the unit circle
    #     a = p[0] ** 2 + p[1] ** 2
    #     b = 2 * x * p[0] + 2 * y * p[1]
    #     c = x ** 2 + y ** 2 - 1
    #     t = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    #     x += t * p[0]
    #     y += t * p[1]
    #
    #     # Calculate the normal to the surface of reflection
    #     n = np.array([x, y])
    #     n = n / np.linalg.norm(n)
    #     # Calculate the new momentum after reflection
    #     p = reflect(p, n)
    #
    #     # Save the reflection point
    #     reflection_points.append((x, y))

    # Test the reversibility of the motion
    reversed_reflection_points = reflection_points[::-1]
    deviation = 0
    for i in range(len(n) + 1):
        if np.linalg.norm(np.array(reflection_points[i]) - np.array(reversed_reflection_points[i])) > delta:
            deviation = i
            break

    if deviation == 0:
        print(f"The motion is reversible up to {n} reflections.")
    else:
        print(f"The motion deviates from reversibility after {deviation} reflections.")

    return reflection_points


# Example usage
num_reflections = 10
reflection_points = simulate_billiard(num_reflections)
print(reflection_points)


print("Reverse")

# Initialize the list of reflection points for different values of n
reflection_points_list = []

# Define the range of values of n to simulate
n_values = range(10)

# Simulate the billiard model for each value of n
for n in n_values:
    reflection_points = simulate(n, 1e-6)
    reflection_points_list.append(reflection_points)
