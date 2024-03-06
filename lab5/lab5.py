#PHSX 216 & 218 plotting code
#Brianna Beller
#Updated September 2023

#import packages and libraries, assign shortcut names
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------#
#----------UPDATE THIS SECTION!!!----------

#DATA TO BE PLOTTED
#UPDATE THE VARIABLE NAMES & NUMBERS (LEAVE BRACKETS/PARENTHESES AS IS)
#variable names should start with a letter and must contain only letters, numbers, and underscores


voltage = np.array([0.246, 0.501, 1.005, 2.051, 3.016, 4.048,
                                    5.034, 6.004, 7, 7.95, 8.95, 9.99])

current = np.array([0.003, 0.007, 0.013, 0.026, 0.038, 0.051, 0.063,
                                    0.075, 0.088, 0.1, 0.112, 0.125])

dcurrent = np.array([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001,
                                   0.001, 0.001, 0.001, 0.001])



#Re-assign variables as x, y, dy so that the remaining plotting code may remain generic
#UPDATE VARIABLE NAMES (ON RHS OF EACH EQUAL SIGN) TO MATCH VARIABLE NAMES FOR DATA ABOVE

x = voltage         #this should be the array you want to plot on the x axis
y = current           #this should be the array you want to plot on the y axis
dy = dcurrent        #this should be your error in y array


#UPDATE EACH OF THESE 4 STRINGS FOR YOUR PLOT LABELS AS YOU WANT THEM TO APPEAR

plot_title= 'The current applied through a resistor increases as the voltage increase'
x_label= 'Voltage (V)'
y_label= 'Current (A)'
slope_units= 'Resistance (Ohms)'

#UPDATE ANNOTATION PLACEMENT SO IT'S OUT OF WAY OF PLOTTED DATA AND BEST FIT LINE
#integer from 1 to 4, top R corner is 1 (counter-clockwise from there)

annotation_placement=2


#-----------------------------------------------------------------------#
#-----DON'T NEED TO CHANGE ANYTHING BEYOND THIS POINT!!!-----


#Find the intercept and slope, b and m, from Python's polynomial fitting function
b,m=np.polynomial.polynomial.polyfit(x,y,1,w=dy)

#Write the equation for the best fit line based on the slope and intercept
fit = b+m*x

#Calculate the error in slope and intercept

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

#assign annotation positions based on annotation_placement value
if annotation_placement==2 or annotation_placement==3:
    xpos=0.05
elif annotation_placement==1 or annotation_placement==4:
    xpos=0.75

if annotation_placement==1 or annotation_placement==2:
    ypos=[.9,.85,.8,.75]
elif annotation_placement==3 or annotation_placement==4:
    ypos=[.2,.15,.1,.05]

#-----------------------------------------------------------------------#
#Don't need to change anything in this section!

#Plot data on graph. Plot error bars and place values for slope,
#error in slope, and vertical intercept (plus error) on the plot using "annotate"

plt.figure(figsize=(15,10))

plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(plot_title)

plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none") #don't need to plot x error bars

plt.annotate('Slope ({}) = {value:.{digits}E}'.format(slope_units,value=m, digits=3),
             (xpos, ypos[0]), xycoords='axes fraction')

plt.annotate('Error in Slope ({}) = {value:.{digits}E}'.format(slope_units,value=dm, digits=3),
             (xpos, ypos[1]), xycoords='axes fraction')

plt.annotate('Vertical intercept = {value:.{digits}E}'.format(value=b, digits=3),
             (xpos, ypos[2]), xycoords='axes fraction')

plt.annotate('Error in vertical intercept = {value:.{digits}E}'.format(value=db, digits=3),
             (xpos, ypos[3]), xycoords='axes fraction')

plt.show()