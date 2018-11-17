import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.interpolate import Rbf
filename = 'Centroids.csv'
data = np.loadtxt(filename, dtype=str, delimiter=',', usecols=range(10), skiprows=1)
GEOID = data[:,0]
LON = data[:,8].astype(float)
LAT = data[:,9].astype(float)
AREA = data[:,7].astype(float)

lonlat = np.transpose([LON,LAT])

# interpolating
loni = np.arange(min(LON), max(LON), 0.01)
lati = np.arange(min(LAT), max(LAT), 0.01)
loni,lati =np.meshgrid(loni,lati)
valuei = griddata((LON,LAT),AREA, (loni,lati), method='cubic', rescale=True)
plt.imshow(valuei,cmap='jet', extent=[min(LON),max(LON),min(LAT),max(LAT)], origin='lower', interpolation='bilinear')
plt.colorbar()
plt.scatter(LON,LAT, c='black', s=0.01)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
