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
        return np.array([t, dt, x0, v0])

    def move(self, t, dt, x0):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        return np.array([t, dt, x0])

    def move(self, t0, t1, dt, x0, v0):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        return np.array([t0, t1, dt, x0, v0])

    def move(self, t0, t1, dt, x0, v0, m):
        """
        Overloaded public method that returns an array of coordinates of an oscillating mass
        """
        return np.array([t0, t1, dt, x0, v0, m])

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


