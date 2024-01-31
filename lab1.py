#-------------------
# Lab1 electric potential
#---------------------
# Myra Jan 31 2024
# ----------------
# requires venvPhysics

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

radiusMillimeters = [10,15,20,25,30,35,40,45,50,55,60,65,70]
channel1 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13], index=radiusMillimeters)
channel2 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13], index=radiusMillimeters)
channel3 = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13], index=radiusMillimeters)

dataTotal = pd.DataFrame(data=(channel1, channel2, channel3)).transpose()
meanVoltage = dataTotal.mean(axis=1)
changeVoltage = meanVoltage.diff()

electricField = -1*(changeVoltage/0.005)




