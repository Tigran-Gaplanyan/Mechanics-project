import math

import numpy as np


class Spring:
    def __init__(self, k=1.0):
        self.__k = k

    @classmethod
    def with_stiffness(cls, k):
        """
        Overloaded constructor that creates a spring with a specified stiffness k
        """
        return cls(k)

    def move(self, t, dt, x0, v0):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        # Calculate the angular frequency of the oscillation
        w = math.sqrt(self.__k)

        # Initialize the array of coordinates
        x = np.zeros_like(t)
        x[0] = x0

        # Calculate the number of time steps based on the given time period and time step
        n = int(t / dt)

        # Iterate over each time step
        for i in range(1, n + 1):
            # Calculate the current time
            current_t = i * dt

            # Calculate the current coordinate using the formula for harmonic motion
            current_x = x0 * math.cos(w * current_t) + (v0 / w) * math.sin(w * current_t)

            # Append the current coordinate to the array
            x[i] = current_x

        # Return the array of coordinates
        return x

    def move(self, t, dt, x0):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        # Calculate the angular frequency of the oscillation
        w = math.sqrt(self.__k)

        # Initialize the array of coordinates
        x = np.zeros_like(t)
        x[0] = x0

        # Calculate the number of time steps based on the given time period and time step
        n = int(t / dt)

        # Iterate over each time step
        for i in range(1, n + 1):
            # Calculate the current time
            current_t = i * dt

            # Calculate the current coordinate using the formula for harmonic motion
            current_x = x0 * math.cos(w * current_t)

            # Append the current coordinate to the array
            x[i] = current_x

        # Return the array of coordinates
        return x

    def move(self, t0, t1, dt, x0, v0):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        w = math.sqrt(self.__k)
        t = np.arange(t0, t1, dt)
        x = x0 * np.cos(w * t) + (v0 / w) * np.sin(w * t)
        return x

    def move(self, t0, t1, dt, x0, v0, m):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        w = math.sqrt(self.__k / m)
        t = np.arange(t0, t1, dt)
        x = x0 * np.cos(w * t) + (v0 / w) * np.sin(w * t)
        return x

    def force(self, x):
        """
        Calculates the force exerted by the spring at displacement x
        """
        return -self.__k * x

    def potential_energy(self, x):
        """
        Calculates the potential energy stored in the spring at displacement x
        """
        return 0.5 * self.__k * x ** 2

    def get_stiffness(self):
        """
        Public getter method that returns the stiffness of the spring
        """
        return self.__k

    def __set_stiffness(self, k):
        """
        Private setter method that sets the stiffness of the spring to k
        """
        self.__k = k

    def in_series(self, that):
        """
        Public method that connects this spring with the provided spring in series and returns a new Spring object
        that represents the equivalent spring.

        that: Spring object that will be connected in series with this Spring object.
        """
        k_eq = self.__k + that.get_stiffness()
        return Spring(k_eq)

    def in_parallel(self, that):
        """
        Public method that connects this spring with the provided spring in parallel and returns a new Spring object
        that represents the equivalent spring.

        that: Spring object that will be connected in parallel with this Spring object.
        """
        k_eq = 1.0 / (1.0 / self.__k + 1.0 / that.get_stiffness())
        return Spring(k_eq)


