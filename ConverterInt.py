from Converter import Converter
from Spring import Spring


class UnitSpring:
    def __init__(self, spring_constant=1):
        self.spring_constant = spring_constant

    def potential_energy(self, displacement):
        return 0.5 * self.spring_constant * displacement ** 2


class ConverterInt(Converter):
    def __init__(self):
        self.spring = Spring(1.0)

    def binary_to_decimal(self, binary):
        decimal = 0
        for i in range(len(binary)):
            decimal += int(binary[i]) * 2 ** (len(binary) - 1 - i)
        return decimal

    def bits_to_springs(self, bits):
        binary_len = len(bits)
        springs = [UnitSpring() for _ in range(binary_len)]
        for i in range(binary_len):
            if bits[binary_len - 1 - i] == '1':
                springs[i] = self.spring
        return springs