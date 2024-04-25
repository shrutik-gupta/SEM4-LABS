#--------------------------------------PLOT GRAPH----------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,1,5.5,10, 6])
ypoints = np.array([0, 250,300,140,870])
plt.subplot(1,2,1)
plt.plot(xpoints, ypoints, 'o--r', ms=10, mfc = 'y') #o= circle marker, -- = dotted, r = red, ms = markersize, mfc, marker face colour

plt.xlabel("Chattisgarh votes")
plt.ylabel("Booth Number")
plt.title("Chattisgarh", loc='left') #moves the title to left
plt.grid(color = 'y') #adds grid to the plot => default parameter = both, else = axis = 'x' or axis =  'y'

x1points = np.array([1,2,3,4,5])
y1points = np.array([10,20,30,40,50])
plt.subplot(1,2,2)
plt.plot(x1points, y1points,'o-b', ms=10, mfc = 'r', mec='r') #mec = marker edge colour

plt.xlabel("Maharashtra votes")
plt.ylabel("Booth Number")
plt.title("Maharashtra", loc='left') 
plt.grid(color = 'y') 

plt.suptitle("Voting Information")
plt.show()
"""

#---------------------------------BAR GRAPH--------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,1,4,10, 6])
ypoints = np.array([70, 250,300,140,870])
myColors = ["hotpink", "green", "#000000", "blue", "orange"]
myLabel = ["Java", "ReactJS", "NodeJS", "PHP", "Angular"]
plt.bar(xpoints, ypoints, width=0.4, color = myColors, tick_label= myLabel) 
plt.xlabel("Languages")
plt.ylabel("Users")
#plt.barh(xpoints, ypoints, height=0.4) -> for horizontal bar, and height insted of width
plt.show()
"""

#---------------------------------HISTOGRAM--------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.random.normal(170, 10, 250)

plt.hist(xpoints,color='r') 
plt.show()
"""

#---------------------------------PIECHART--------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
myLabels = ["Java", "ReactJS", "NodeJS", "PHP"]
myExplode= [0.2,0,0.4,0] #first section will explode 20%, second section 0% and so on
myColors = ["pink", "green", "#000000", "blue"]

plt.pie(y, labels=myLabels, startangle=90, explode = myExplode, shadow=True, colors = myColors)
plt.legend(title="Popularity")
plt.show()  

