from abc import ABC, abstractmethod
import numpy as np
from Spring import Spring
from typing import List
from Body import Body


class Converter(ABC):
    @abstractmethod
    def binary_to_decimal(self, binary):
        pass

    @abstractmethod
    def bits_to_springs(self, bits):
        pass

    def compute_oscillations(self, bits: str, t: float, dt: float, x0: float, vo: float) -> List[float]:
        springs = self.bits_to_springs(bits)
        spring = springs[0]
        for i in range(1, len(springs)):
            spring = spring.in_series(springs[i])
        body = Spring(1.0, spring)
        return body.move(t, dt, x0, vo)

    def connect_body_to_springs(self, springs):
        body = Body(1, springs)
        return body.move(10, 0.01, 0, 0)

    def calculate_frequency_amplitudes(self, bits: List[int]):
        springs = self.convert_bits_to_springs(bits)
        oscillations = self.connect_body_to_springs(springs)
        n = len(oscillations)
        dt = 0.01
        freqs = np.fft.fftfreq(n, dt)[:n // 2]
        fft = np.fft.fft(oscillations)[:n // 2]
        amplitudes = 2.0 / n * np.abs(fft)
        return freqs, amplitudes

    def evaluate_decimal_value(self, bits: List[int]):
        freqs, amplitudes = self.calculate_frequency_amplitudes(bits)
        decimal_value = 0
        for i in range(len(amplitudes)):
            decimal_value += amplitudes[i] * freqs[i]
        return decimal_value