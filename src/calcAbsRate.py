# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:00:46 2023

@author: alanc
"""
import math

def calcAbsRate(realPerm, u, cond, z, E):
    # realPerm is real part of permittivity
    # u is permeability
    # cond is conductivty
    # z is thickness of layer
    # E is amplitude of wave signal
    w = 2000 #changes based on input wave
    imagPerm = cond/w
    absPerm = math.sqrt((imagPerm ** 2) * (realPerm ** 2))
    a = w * math.sqrt(u/ (2 * (realPerm + absPerm)) * imagPerm)
    EB = E * math.exp(-a * z)
    return EB