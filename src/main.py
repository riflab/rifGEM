import numpy as np
import FFMT1D
import matplotlib.pyplot as plt
import plot_PerRhoPhase

min_freq = 0.01
total_dec = 5	
freq_per_dec = 10

nfreq = total_dec*freq_per_dec+1
frac = np.exp(np.log(10) /freq_per_dec)

freq = []
freq.append(min_freq)

for i in range (1,nfreq):
	freq.append(freq[i-1]*frac)

per = []
nper = len(freq)
for i in range (0,nper):
	per.append(1/freq[i])

res = [100, 1, 1000]
thi = [100, 1000]

rho, phas = FFMT1D.FFMT1D(res,thi, per)
print(rho, phas)
plot_PerRhoPhase.plot_PerRhoPhase(per, rho, phas)