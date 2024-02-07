#-------------------
# Lab1 electric potential
#---------------------
# Myra Jan 31 2024
# ----------------
# requires venvPhysics

#packages 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import statistics

#creating lists for use later
#radiusMid = list()

#data
radiusMillimeters = [10,15,20,25,30,35,40,45,50,55,60,65,70]
channelA = np.array([(18.2,15.6,12.6,11.5,9.1,8.8,7.5,6.7,5.7,4.9,4.0,3.1,2.3),(radiusMillimeters)])
channelB = np.array([(16.6,14.1,11.6,10.0,8.8,7.5,6.5,5.6,5.1,4.3,3.7,3.2,2.7),(radiusMillimeters)])
channelC = np.array([(16.0,13.5,11.8,9.5,8.4,7.3,6.4,5.4,4.6,4.1,3.5,3.1,2.7),(radiusMillimeters)])

#analysis
dataTotal = np.array([(channelA),(channelB),(channelC)])
meanVoltage = dataTotal[:,0].mean(axis=0)
diffVoltage = np.diff(meanVoltage)
electricField = -(diffVoltage/0.005)
radiusMid = [(radiusMillimeters[i]/1000 + radiusMillimeters[i+1]/1000)/2 for i in range(len(radiusMillimeters)-1)]
x = np.array([math.log(k) for k in radiusMid])
y = np.array([math.log(j) for j in electricField])

#error
d_meanVoltage = np.std(dataTotal[:,0], axis=0)/math.sqrt(3)
d_Radius = 0.001
d_diffVoltage = np.array([(d_meanVoltage[i]**2+d_meanVoltage[i-1]**2)**0.5 for i in range(1,13)])
d_diffRadius = math.sqrt(0.001**2 + 0.001**2)
test = (d_diffVoltage/diffVoltage)**2
d_electricField = abs(electricField)*(
    (d_diffVoltage/diffVoltage)**2
    + (-d_diffRadius/0.001)**2
    )**0.5
dy = abs(np.log(y)-np.log(y+d_electricField))
dx = abs(np.log(x)-np.log(x+d_diffRadius))

#Find the intercept and slope, b and m, from Python's polynomial fitting function
b,m=np.polynomial.polynomial.polyfit(x,y,1,w=dy)

#Write the equation for the best fit line based on the slope and intercept
fit = b+m*x

#error in slop
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D

D=Delta(x, dy)

dm = np.sqrt(1/D*sum(1/dy**2)) #error in slope
db = np.sqrt(1/D*sum(x**2/dy**2)) #error in intercept

#Calculate the "goodness of fit" using linear least squares fitting
#(value close to number of plotted points indicates good fit)
def LLSFD2(x,y,dy):
    N = sum(((y-b-m*x)/dy)**2)
    return N

N = LLSFD2(x,y,dy)

#annotation info
annotation_placement=2
if annotation_placement==2 or annotation_placement==3:
    xpos=0.05
elif annotation_placement==1 or annotation_placement==4:
    xpos=0.75

if annotation_placement==1 or annotation_placement==2:
    ypos=[.9,.85,.8,.75]
elif annotation_placement==3 or annotation_placement==4:
    ypos=[.2,.15,.1,.05]

#plotting
plt.figure(figsize=(15,10))

plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')

plt.xlabel('Ln(radius)')
plt.ylabel('Ln(Electric Field)')
plt.title('Logarithmic Relationship between the Radius from a Charge and the Magnitude of the Electric Field' )
plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars
plt.annotate('Slope ({}) = {value:.{digits}E}'.format('',value=m, digits=3),
             (xpos, ypos[0]), xycoords='axes fraction')

plt.annotate('Error in Slope ({}) = {value:.{digits}E}'.format('',value=dm, digits=3),
             (xpos, ypos[1]), xycoords='axes fraction')

plt.annotate('Vertical intercept = {value:.{digits}E}'.format(value=b, digits=3),
             (xpos, ypos[2]), xycoords='axes fraction')

plt.annotate('Error in vertical intercept = {value:.{digits}E}'.format(value=db, digits=3),
             (xpos, ypos[3]), xycoords='axes fraction')

plt.show()
print('m')
