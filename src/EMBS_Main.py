import calcAbsRate
import calcPowerDensity
import reflectionLoss
import numpy as np
import pandas as pd

def main():

    lung_matrix = pd.read_csv("lung.csv").to_numpy()

    tskin = 
    rhoskin = 1
    rel_permskin = 44.5

    tfat = 
    rhofat = 9.35
    rel_permfat = 6.4

    tmuscle = 
    rhomuscle = 0.77
    rel_permmuscle = 50.5

    human_list_of_tups = [(tskin, rhoskin, rel_permskin), (tfat, rhofat, rel_permfat), (tmuscle, rhomuscle, rel_permmuscle), (-1, rholung, rel_permlung)]

    for 
if __name__ == "__main__":
    main()