from Converter import Converter
from ConverterInt import ConverterInt


class ConverterFloat(Converter):

    def __init__(self, integer_bits, fraction_bits):
        super().__init__()
        self.integer_bits = integer_bits
        self.fraction_bits = fraction_bits
        self.integer_converter = ConverterInt()
        self.fraction_converter = ConverterInt()

    def binary_to_decimal(self, binary):
        # Fetch the radix point
        point = binary.find('.')

        # Update point if not found
        if (point == -1):
            point = len(binary)

        intDecimal = 0
        fracDecimal = 0
        twos = 1

        # Convert integral part of binary
        # to decimal equivalent
        for i in range(point - 1, -1, -1):
            # Subtract '0' to convert
            # character into integer
            intDecimal += ((ord(binary[i]) -
                            ord('0')) * twos)
            twos *= 2

        # Convert fractional part of binary
        # to decimal equivalent
        twos = 2

        for i in range(point + 1, len(binary)):
            fracDecimal += ((ord(binary[i]) -
                             ord('0')) / twos)
            twos *= 2.0

        # Add both integral and fractional part
        ans = intDecimal + fracDecimal

        return ans

    def bits_to_springs(self, bits):
        integer_part = bits[:self.integer_bits]
        fraction_part = bits[self.integer_bits:]

        integer_springs = self.integer_converter.bits_to_springs(integer_part)
        fraction_springs = self.fraction_converter.bits_to_springs(fraction_part)

        springs = integer_springs + fraction_springs
        return springs