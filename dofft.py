# Function file : dofft.py
# Info          : Discrete Fourier Transform (DFT) Program
# Written by    : Aulia Khalqillah, S.Si., M.Si.
# Update        : 10th March, 2020
#---------------------------------------------------------------------------
from math import *
from numpy import *

def dofft(signal,nfft,fs):
    N = len(signal)
    if N <= nfft:
        rod = nfft-N
        zerpad = list(zeros(rod))
        signal.extend(zerpad)

    fstep = fs
    dt = 1.0/fs
    fr = 0
    freq = []
    j = 0

    n = 0
    spectrum = []
    while n < nfft:
        k = 0
        sreal = 0.0
        specreal = []
        simag = 0.0
        specim = []
        while k < nfft:
            sreal = sreal + (signal[k]*cos(2*pi*k*n/nfft))
            simag = simag + (signal[k]*sin(2*pi*k*n/nfft))
            k = k + 1

        fr = fr + (fstep/nfft)
        freq.append(fr)
        spectrum.append(abs(complex(sreal,simag)))
        n = n + 1
    return freq, spectrum
