from Converter import Converter
from Spring import Spring

class Converter8Bit(Converter):
    def __init__(self):
        self.springs = []

    def binary_to_decimal(self, binary):
        decimal = 0
        for bit in binary:
            decimal = decimal * 2 + int(bit)
        return decimal

    def bits_to_springs(self, bits):
        n = len(bits)
        if n == 0:
            return self.springs
        elif n == 1:
            if bits[0] == '0':
                return self.springs + [Spring(1)]
            else:
                return self.springs + [Spring(2)]
        else:
            mid = n // 2
            left = self.bits_to_springs(bits[:mid])
            right = self.bits_to_springs(bits[mid:])
            if bits[0] == '0':
                return self.springs + [Spring.inSeries(left[-1], right[0])] + left[:-1] + right[1:]
            else:
                return self.springs + [Spring.inParallel(left[-1], right[0])] + left[:-1] + right[1:]

    # def to_spring_system(self, bits: str):
    #     if len(bits) != 8:
    #         raise ValueError("Input must be 8 bits long.")
    #     springs = []
    #     for i in range(len(bits)):
    #         if bits[i] == "1":
    #             springs.append(self.springs[i])
    #     return springs
    #
    # def from_spring_system(self, spring_system) -> int:
    #     value = 0
    #     for i in range(len(spring_system)):
    #         if spring_system[i] > 0:
    #             value += self.springs[i]
    #     return value