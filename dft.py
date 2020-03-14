# Name          : dft.py
# Info          : Discrete Fourier Transform (DFT) Program
# Function file : dofft.py
# Written by    : Aulia Khalqillah, S.Si., M.Si.
# Update        : 10th March, 2020
#---------------------------------------------------------------------------
import math as m
import csv
import matplotlib.pyplot as plt
from numpy import arange
from random import random
from scipy.fftpack import fft
from dofft import dofft # call function file dofft.py

# SIGNAL
f1 = 20
time = 0.0
dt = 0.01
signal = [];
signal_rand = [];
t = [];
i = 0
n = 2000
while i < n:
    x = m.sin(2*m.pi*f1*time)
    xrd = x*random()
    signal.append(x)
    signal_rand.append(xrd)
    t.append(time)
    time = time + dt
    i = i + 1

print("Length of Data: ", len(signal_rand))

with open("signal.csv","w") as f:
    fsignal = csv.writer(f, delimiter='\t')
    fsignal.writerows(zip(t,signal,signal_rand))

topbound = 0.92
bottombound = 0.08
leftbound = 0.10
rightbound = 0.95
heighspace = 0.5
widthspace = 0.35
fig = plt.figure(1)
fig1 = fig.add_subplot(211)
plt.plot(t,signal,color='black', linewidth=0.5, label='Signal')
plt.title('Sinusoidal Signal and Random Signal')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.grid()
plt.subplots_adjust(top=topbound, bottom=bottombound, left=leftbound, right=rightbound, hspace=heighspace,wspace=widthspace)

fig2 = fig.add_subplot(212)
plt2 = plt.plot(t,signal_rand, color='red', linewidth=0.5, label='Random Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend(loc='upper left')
plt.grid()
plt.subplots_adjust(top=topbound, bottom=bottombound, left=leftbound, right=rightbound, hspace=heighspace,wspace=widthspace)


# DFT from function file
fs = 100
nfft = 1024
freq, spectrum = dofft(signal_rand,nfft,fs)

# FFT from Python Library
pyspectrum = fft(signal_rand,nfft)
freq2 = arange(0,len(pyspectrum))/(nfft/fs)

maxspec1 = max(spectrum)
maxspec2 = max(abs(pyspectrum))
id_maxspec1 = argmax(spectrum)
id_maxspec2 = argmax(abs(pyspectrum))
freq_spectrum = freq[id_maxspec1]
freq_pyspectrum = freq2[id_maxspec2]

print("Length of FFT from python: ",len(pyspectrum))
print("Length of DFT from function: ",len(spectrum))
print("Frequency from FFT Library:", freq_pyspectrum)
print("Frequency from DFT Function:", freq_spectrum)

# Plot Spectrum Comparison
figspec = plt.figure(2)
fig3 = figspec.add_subplot(211)
plt.plot(freq,spectrum,color='black', linewidth=0.5, label='Spectrum')
plt.title('DFT from written function')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectrum')
plt.legend(loc='upper left')
plt.grid()
plt.subplots_adjust(top=topbound, bottom=bottombound, left=leftbound, right=rightbound, hspace=heighspace,wspace=widthspace)

fig4 = figspec.add_subplot(212)
plt.plot(freq2, abs(pyspectrum),color='black', linewidth=0.5, label='Spectrum')
plt.title('FFT from Python Library')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectrum')
plt.legend(loc='upper left')
plt.grid()
plt.subplots_adjust(top=topbound, bottom=bottombound, left=leftbound, right=rightbound, hspace=heighspace,wspace=widthspace)
plt.show()
