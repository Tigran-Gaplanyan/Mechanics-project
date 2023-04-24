import math
from Converter import Converter
from Spring import Spring


class ConverterFloat(Converter):

    def __init__(self, int_bits, frac_bits):
        self.int_bits = int_bits
        self.frac_bits = frac_bits

    def binary_to_decimal(self, binary):
        # Split the binary string into integer and fractional parts
        int_str = binary[:self.int_bits]
        frac_str = binary[self.int_bits:]

        # Convert the integer part to decimal
        int_part = self.binary_to_decimal_int(int_str)

        # Convert the fractional part to decimal
        frac_part = self.binary_to_decimal_frac(frac_str)

        # Combine the integer and fractional parts
        return int_part + frac_part

    def binary_to_decimal_int(self, binary):
        # Convert the integer part to decimal
        decimal = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** (len(binary) - i - 1)
        return decimal

    def binary_to_decimal_frac(self, binary):
        # Convert the fractional part to decimal
        decimal = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** (-1 * (i + 1))
        return decimal

    def bits_to_springs(self, bits):
        # Convert the binary sequence to an array of frequency amplitudes using the Fourier Transform
        freq_amps = self.compute_freq_amps(bits)

        # Create a system of unit springs that implements the frequency amplitudes
        spring_system = self.create_spring_system(freq_amps)

        return spring_system

    def compute_freq_amps(self, bits):
        # Compute the frequency amplitudes of the oscillations using the Fourier Transform
        N = len(bits)
        freq_amps = []
        for k in range(N):
            amplitude = 0
            for n in range(N):
                amplitude += int(bits[n]) * math.cos(2 * math.pi * k * n / N)
            freq_amps.append(amplitude)
        return freq_amps

    def create_spring_system(self, freq_amps):
        # Create a system of unit springs that implements the frequency amplitudes
        spring_system = []
        for freq_amp in freq_amps:
            spring_system.append(Spring(k=abs(freq_amp)))
        return spring_system
