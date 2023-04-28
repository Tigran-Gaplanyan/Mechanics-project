from math import sqrt

from Converter import Converter
from Spring import Spring


class ConverterInt(Converter):
    def __init__(self):
        self.spring = Spring(1.0)

    def binary_to_decimal(self, binary):
        decimal = 0
        for i in range(len(binary)):
            decimal += binary[i] * 2 ** (len(binary) - 1 - i)
        return decimal

    def bits_to_springs(self, bits):
        n = len(bits)
        s = sqrt(2)
        springs = []
        for i in range(n):
            if bits[i] == 1:
                springs.append(Spring(spring_constant=s))
            else:
                springs.append(Spring(spring_constant=1 / s))
        for i in range(n - 1):
            springs[i].in_series(springs[i + 1])
        return springs[0]