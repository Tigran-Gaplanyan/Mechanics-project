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
                return self.springs + [Spring.in_series(left[-1], right[0])] + left[:-1] + right[1:]
            else:
                return self.springs + [Spring.in_parallel(left[-1], right[0])] + left[:-1] + right[1:]