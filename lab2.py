#importing packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data cleaning up steps:
# 1) delete column names if they exist
# 2) delete the last column (scan retry)

#loading data- change path
data = pd.read_csv(, low_memory = False)
count = 0

#converting time data to integer values- change row data
time = pd.to_datetime(data.iloc[4:, 0], format = '%m/%d/%Y %H:%M')
deltaTimev1 = (time-time.iloc[0])
deltaTime = deltaTimev1.dt.total_seconds()

#name generation for instruments
names = ["GeoFlex" + str(i) for i in range(1,51,1)]

tiltX = data.iloc[4:, :].iloc[:, range(5, 202, 4)].set_axis([names], axis="columns")
tiltY = data.iloc[4:, :].iloc[:, range(6, 203, 4)].set_axis([names], axis="columns")
voltage = data.iloc[4:, :].iloc[:, range(7, 204, 4)].set_axis([names], axis="columns")
tempC = data.iloc[4:, :].iloc[:, range(8, 205, 4)].set_axis([names], axis="columns")

#removing NaN values without changing index
tiltXWithoutNaN = tiltX.join(deltaTime).dropna().astype(float)
tiltYWithoutNaN = tiltY.join(deltaTime).dropna().astype(float)
tempCWithoutNaN = tempC.join(deltaTime).dropna().astype(float)
voltageWithoutNaN = voltage.join(deltaTime).dropna().astype(float)

#calculations for displacement (equations provided by GeoFlex documentation)
displacementMagnitudeX = (tiltXWithoutNaN.iloc[:,0:50]*0.6).diff(axis=0).dropna().join(deltaTime).rename(columns={"Column1":"Time"})
displacementMagnitudeY = (tiltYWithoutNaN.iloc[:,0:50]*0.6).diff(axis=0).dropna().join(deltaTime).rename(columns={"Column1":"Time"})

#some good ol pythagorean
displacementTotal = pd.DataFrame(np.sqrt((
abs(displacementMagnitudeX.iloc[:,0:50])**2)+(
abs(displacementMagnitudeY.iloc[:,0:50])**2))).join(deltaTime).rename(columns={"Column1":"Time"})

#converting from cartesian to polar to find angles
displacementAngle = (np.arctan2(displacementMagnitudeY.iloc[:,0:50],displacementMagnitudeX.iloc[:,0:50])*180/np.pi).join(
deltaTime).rename(columns={"Column1":"Time"})

#plotting
plt.rcParams.update({'font.size': 7})
fig = plt.figure(layout='constrained')
spec = fig.add_gridspec(2,2)

#plot2
ax1 = fig.add_subplot(spec[1,0])
ax1.scatter(tempCWithoutNaN.iloc[1:,0:50], np.abs(displacementTotal.iloc[:,0:50]), marker=".", facecolor='C9', edgecolor='k')
ax1.axis([-12,12,0,0.2])
ax1.set_xlabel("Degrees Centigrade")
ax1.set_ylabel("Magnitude of Displacement of Sensor [mm]")

#plot3
ax2 = fig.add_subplot(spec[1,1])
ax2.hist(displacementAngle.iloc[:,0:49], bins=90, stacked=True)
ax2.axis([-180, 180, 0, 400])
ax2.set_xlabel("Degrees from positive X-axis (bins=2 degrees)")
ax2.set_ylabel("Number of occurences (n)")

#plot1
ax3 = fig.add_subplot(spec[0,:])
ax3.plot(displacementTotal.iloc[:,50],displacementTotal.iloc[:,0:4], ls=':', linewidth='0.7')
ax3.axis([0,525000,0,0.3])
ax3.set_xlabel("Time[minutes]")
ax3.set_ylabel("Magnitude of Displacement of Sensor [mm]")
ax3.set_title("Fig 1: Seismogram")

plt.show()