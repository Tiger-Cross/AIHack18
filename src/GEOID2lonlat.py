import numpy as np
import pandas as pd
filepath = '../data/raw/california/train/'
filename = 'X15_EDUCATIONAL_ATTAINMENT.csv'
datafile = 'Centroids.csv'

data = np.loadtxt(datafile, dtype=str, skiprows=1, delimiter=',', usecols=range(10))
#df = pd.read_csv(datafile)
#print df

GEOID=data[:,0]
AREA=data[:,7].astype(float)
LON=data[:,8].astype(float)
LAT=data[:,9].astype(float)

lonlat = np.transpose([LON,LAT])
D = {}
for i in range(len(lonlat)):
    D[GEOID[i]] = tuple(lonlat[i])

print D
