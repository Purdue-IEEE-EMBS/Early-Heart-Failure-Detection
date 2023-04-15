# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:00:46 2023

@author: alanc
"""
import math

def calcAbsRate(rel_perm, cond, z, E, w):
    # realPerm is real part of permittivity
    # u is permeability
    # cond is conductivty
    # z is thickness of layer
    # E is amplitude of wave signal
    imagPerm = cond/w
    abs_perm = 8.85419e-12
    u = 1.25663706e-6
    realPerm = abs_perm * rel_perm

    magPerm = math.sqrt((imagPerm ** 2) + (realPerm ** 2))
    a = w * math.sqrt(u / (2 * (realPerm + magPerm)) * imagPerm)
    E_B = E * math.exp(-a * z)

    return E_B