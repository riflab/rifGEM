import numpy as np


def calculate_RhoPhase(zr, zi, freq):
    RHO = []
    PHASE = []
    per = []
    for i in range(0, len(freq)):
        per.append(float(1 / (float(freq[i]))))
        RHO.append((0.2 * float(1 / (float(freq[i])))) * (np.abs(complex(float(zr[i]), float(zi[i])))) ** 2)
        PHASE.append(np.degrees(np.arctan(((float(zi[i]) / float(zr[i]))))))

    return per, RHO, PHASE
