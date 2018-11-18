import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from scipy.interpolate import Rbf
from shapely.geometry.polygon import Polygon
from shapely.geometry import Point
from shapely.geometry import shape
import matplotlib.cm as cm

filename = 'Centroids.csv'
data = np.loadtxt(filename, dtype=str, delimiter=',', usecols=range(10), skiprows=1)
GEOID = data[:,0]
LON = data[:,8].astype(float)
LAT = data[:,9].astype(float)

# CHANGE THIS, e.g. X19_INCOME.csv, X15_EDUCATIONAL_ATTAINMENT.csv
CSV_file = '../data/processed/X15_EDUCATIONAL_ATTAINMENT.csv'
CSV_VARIABLE = np.loadtxt(CSV_file, dtype=str, delimiter=',', usecols=(123,), skiprows=0)
CSV_VARIABLE_NAME = CSV_VARIABLE[0]
CSV_VARIABLE = CSV_VARIABLE[1:].astype(float)

CSV_GEOID = np.loadtxt(CSV_file, dtype=str, delimiter=',', usecols=(2,), skiprows=1)
CSV_LONLAT = np.zeros((len(CSV_GEOID),2), dtype=float)

filename='COUNTYNODES.csv'
data = np.loadtxt(filename, dtype=str, usecols=range(8), skiprows=1, delimiter=',')
COUNTY = data[:,3]
CLON = data[:,6].astype(float)
CLAT = data[:,7].astype(float)

lonlat = np.transpose([LON, LAT])

# dictionary of mapping:
D = {}
for i in range(len(GEOID)):
    D[GEOID[i]] = lonlat[i]

failed=[] # find index of CSV_GEOID err
for i in range(len(CSV_GEOID)):
    try:
        CSV_LONLAT[i] = D[CSV_GEOID[i]]
    except:
        print 'FAILED: %s, INDEX: %d' % (CSV_GEOID[i], i)
#print CSV_LONLAT.shape
        failed.append(i)
# loop backwards
for j in range(len(CSV_LONLAT)-1,-1,-1):
    if j in failed:
        CSV_LONLAT = np.delete(CSV_LONLAT, j, axis=0)
        CSV_VARIABLE = np.delete(CSV_VARIABLE, j, axis=0)
LON = CSV_LONLAT[:,0]
LAT = CSV_LONLAT[:,1]

D={}
lassenlon=[]
lassenlat=[]

countynames = []
for i in COUNTY:
    if i not in countynames:
        countynames.append(i)
Dlon = {}
Dlat = {}
Dlonlat = {}
Dpoly = {}
for j in countynames:
    countylon=[]
    countylat=[]
    countylonlat=[]
    for i in range(len(COUNTY)):
        if COUNTY[i] == j:
            countylon.append(CLON[i])
            countylat.append(CLAT[i])
            countylonlat.append([CLON[i],CLAT[i]])
    Dlon[j] = countylon
    Dlat[j] = countylat

    # TO PLOT COUNTY BORDERS UNCOMMENT
    #plt.plot(countylon, countylat, c='black', linewidth=0.3)

    Dlonlat[j] = countylonlat
    poly = Polygon(countylonlat)
    Dpoly[j] = poly

Dvalue = {}
countycnt=0

# USED TO CALCULATE AVERAGE VALUE OF VARIABLE PER COUNTY:
for i in countynames:
    countyavg=0
    countycnt=0
    for j in range(len(LON)):
        if Dpoly[i].contains(Point(LON[j], LAT[j])):
            countyavg += CSV_VARIABLE[j]
            countycnt += 1
    if countycnt != 0:
        countyavg /= countycnt
        # get percentage assuming 1000 per block group:
        countyavg /= 10
    Dvalue[i] = countyavg

# PLOT POLYGONS
norm = matplotlib.colors.Normalize(vmin=0, vmax=max(Dvalue.values()))
fig = plt.figure()
ax = fig.add_subplot(111)
for i in countynames:
    countypoly = Dpoly[i]
    x,y = countypoly.exterior.xy
    cmap = cm.plasma
    color = cmap(norm(Dvalue[i]))
    
    ax.fill(x,y, c=color)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(CSV_VARIABLE_NAME[:30] + ".pdf")
plt.show()

fig = plt.figure(figsize=(3,8))
ax2 = fig.add_axes([0.05, 0.05, 0.15, 0.9])

cb1 = matplotlib.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='vertical')
cb1.set_label('Percentage of people per Block Group with a Bachelor\'s')
plt.savefig(CSV_VARIABLE_NAME[:30] + "_colorbar.pdf")
plt.show()
