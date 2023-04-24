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

    # def evaluate(self, binary_seq):
    #     # compute the frequency amplitudes of the oscillations
    #     freq_amps = self.calculate_freq_amplitudes(binary_seq)
    #
    #     # determine the maximum frequency amplitude
    #     max_freq_amp = max(freq_amps)
    #
    #     # calculate the decimal value using the maximum frequency amplitude
    #     decimal_val = int(max_freq_amp / self.spring.stiffness)
    #
    #     return decimal_val
    #
    # def create_spring_system(self, binary_seq):
    #     # initialize the first spring
    #     first_spring = self.spring
    #
    #     # initialize the spring system with the first spring
    #     spring_system = [first_spring]
    #
    #     # iterate over the binary sequence and add springs to the system as needed
    #     for i in range(1, len(binary_seq)):
    #         if binary_seq[i] == '1':
    #             # add a new spring in parallel to the existing springs in the system
    #             new_spring = Spring(1.0)
    #             spring_system = [new_spring] + spring_system
    #         else:
    #             # add a new spring in series to the last spring in the system
    #             new_spring = Spring(1.0)
    #             spring_system[-1] = spring_system[-1].inSeries(new_spring)
    #
    #     return spring_system