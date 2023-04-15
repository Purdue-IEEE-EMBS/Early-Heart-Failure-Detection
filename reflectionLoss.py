import math as m
import cmath as cm

def impedance_conversion(conductivity, rel_perm, w, x, y, z, thickness):
    abs_perm = 8.85419e-12
    A = x * z
    L = y * thickness
    rho = 1/conductivity

    R = (rho * L) / A
    C = (rel_perm * abs_perm * A) / L
    Z_C = 1/((1j) * w * C)

    Zeq = (1/R) + (1/Z_C)
    Zeq = 1/Zeq

    return Zeq

def reflection_loss(thickness, power, z1, z2):
    deltaR  = cm.abs((z2 - z1) / (z2 + z1)) ** 2
    nextP = power * (1 - deltaR)
    magE = cm.sqrt(nextP)
    magB = magE

    return magE
