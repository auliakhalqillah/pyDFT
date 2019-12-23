# Name          : dft.py
# Info          : Discrete Fourier Transform (DFT) Program
# Written by    : Aulia Khalqillah, S.Si
# Update        : December, 23 2019
#---------------------------------------------------------------------------
import math as m
import csv
import matplotlib.pyplot as plt
from random import random

# SIGNAL
f1 = 20
time = 0.0
dt = 0.01
signal = [];
signal_rand = [];
t = [];
i = 0
n = 500
while i < n:
    # x = m.sin(m.radians(2*m.pi*f1*time))
    x = m.sin(2*m.pi*f1*time)
    xrd = x*random()
    signal.append(x)
    signal_rand.append(xrd)
    t.append(time)
    print(time,"\t",x,"\t",xrd)
    time = time + dt
    i = i + 1

with open("signal.csv","w") as f:
    fsignal = csv.writer(f, delimiter='\t')
    fsignal.writerows(zip(t,signal,signal_rand))

fig = plt.figure(1)
fig1 = fig.add_subplot(211)
plt.plot(t,signal,color='black', linewidth=0.5, label='Signal')
plt.title('Sinusoidal Signal and Random Signal')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')

fig2 = fig.add_subplot(212)
plt2 = plt.plot(t,signal_rand, color='red', linewidth=0.5, label='Random Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.show()

# DFT
nfft = 1024
N = len(signal_rand)
if N <= nfft:
    nfft = N
else:
    nfft = nfft

fstep = 1/dt
fr = 0
freq = []
j = 0
# while j < nfft:
#     fr = fr + (fstep/nfft)
#     freq.append(fr)
#     j = j + 1

n = 0
spectrum = []
while n < nfft/2:
    k = 0
    sreal = 0.0
    specreal = []
    simag = 0.0
    specim = []
    while k < nfft:
        sreal = sreal + (signal_rand[k]*m.cos(2*m.pi*k*n/nfft))
        specreal.append(sreal)
        simag = simag + (signal_rand[k]*m.sin(2*m.pi*k*n/nfft))
        specim.append(simag)
        k = k + 1

    fr = fr + (fstep/nfft)
    freq.append(fr)
    spec = ((specreal[n]*specreal[n]) + (specim[n]*specim[n]))*dt
    spectrum.append(spec)
    n = n + 1

with open("spectrum.csv","w") as sp:
    fspectrum = csv.writer(sp, delimiter='\t')
    fspectrum.writerows(zip(freq,spectrum))

figspec = plt.figure(2)
# fig1 = fig.add_subplot(211)
plt.plot(freq,spectrum,color='black', linewidth=0.5, label='Spectrum')
plt.title('DFT')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectrum')
plt.legend(loc='upper left')
plt.show()
