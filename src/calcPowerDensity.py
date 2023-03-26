import math

def calcPowerDensity(E, B):
    S = (E*B) / (4 * math.pi * 10**(-7))
    return S