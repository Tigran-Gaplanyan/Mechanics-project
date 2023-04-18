import math

import numpy as np
from typing import List


class FT:
    def __init__(self, x):
        self.N = len(x)
        self.real = np.zeros(self.N)
        self.imag = np.zeros(self.N)

        for k in range(self.N):  # loop over all frequency bins
            for n in range(self.N):  # loop over all time samples
                angle = 2 * np.pi * k * n / self.N
                self.real[k] += x[n] * np.cos(angle)
                self.imag[k] -= x[n] * np.sin(angle)

    def get_spectrum(self):
        return np.sqrt(self.real ** 2 + self.imag ** 2)

    def get_phase(self):
        return np.arctan2(self.imag, self.real)

    def get_frequency(self, k):
        return k / self.N

    def fourier_transform(self, x: List[float]) -> List[float]:
        N = len(x)
        amplitudes = []
        for k in range(N):
            ak = 0.0
            for n in range(N):
                ak += x[n] * math.sin(2 * math.pi * k * n / N)
            ak /= N / 2.0
            amplitudes.append(ak)
        return amplitudes