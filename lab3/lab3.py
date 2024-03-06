#importing packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#experiment one
time = pd.Series([0,10,20,30,40,50,60,70,80,90,100,110,120]) #d_time 0.2
voltageChargingExperiment1 = pd.Series([0,3.714,6.048,7.53,8.33,8.81,9.19,9.46,9.62,9.78,9.94,10.11,10.29]) #d_V 0.05
voltageDischargingExperiment1 = pd.Series([11.29,7.91,5.46,3.82,2.63,1.87,1.3,0.918,0.65,0.46,0.34,0.25,0.188])

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.scatter(time, voltageChargingExperiment1)
ax1.set_title('Voltage Charging Over Time')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Voltage')
ax2.scatter(time, voltageDischargingExperiment1)
ax2.set_title('Voltage Discharging Over Time')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Voltage')

#experiment two
timeChargingExperiment2 = pd.Series([27.89,27.79,27.73,27.59,27.79,27.59,27.49,27.73,27.53])
timeDischargingExperiment2 = pd.Series([26.31,25.93,25.93,25.79,25.91,26.19,25.93,25.79,25.93])
voltage0 = 11.44
voltageD = 4.209
voltageC = 7.23

meanTauCharge2 = np.mean(timeChargingExperiment2)
meanTauDischarge2 = np.mean(timeDischargingExperiment2)
d_timeChargingExperiment2 = np.std(timeChargingExperiment2)/np.sqrt(len(timeChargingExperiment2))
d_timeDischargingExperiment2 = np.std(timeDischargingExperiment2)/np.sqrt(len(timeDischargingExperiment2))

#experiment three
resistanceMeasured = 504.0
capacitance = 53.2

tauTheoretical = 504000*0.000053
d_tauTheoretical = tauTheoretical*np.sqrt((1/504)**2+
                                          (0.1/53.2)**2)

plt.show()

