from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

print "Running..."

#sc_bdm
clat_1,clon_1 = np.loadtxt('file.txt', usecols=(0,1), unpack=True)

#Lat e lon
#lat_low   = -49.00
#lat_high  =  11.00
#lon_left  = 280.00
#lon_right = 325.00

map = Basemap(projection='mill',
    resolution = 'h',
    llcrnrlon=lon_left, llcrnrlat=lat_low,
    urcrnrlon=lon_right, urcrnrlat=lat_high)

map.drawcoastlines(linewidth=0.1)
map.drawcountries(linewidth=0.1)
map.fillcontinents(color='#f4f4f4', lake_color='#d6f0ff', zorder=0)
map.drawmapboundary(fill_color='#d6f0ff', linewidth=0.1)
map.drawmeridians(np.arange(0,360,60),labels=[0,0,0,1], color='gray', fontsize=8, linewidth=0.2)
map.drawparallels(np.arange(-90,90,20),labels=[1,0,0,0], color='gray', fontsize=8, linewidth=0.2)

map.drawstates(color='0.5')

#blue
x_1,y_1 = map(clon_1,clat_1)
map.scatter(x_1,y_1,4,marker='o',lw=0, c='#0000cd', label='LEG1')

#brown
x_2,y_2 = map(clon_2,clat_2)
map.scatter(x_2,y_2,4,marker='o',lw=0, c='#8b4513', label='LEG2')

#yellow
x_3,y_3 = map(clon_3,clat_3)
map.scatter(x_3,y_3,4,marker='o',lw=0, c='#ffd700', label='LEG3')

#deep pink
x_4,y_4 = map(clon_4,clat_4)
map.scatter(x_4,y_4,4,marker='o',lw=0, c='#ff1493', label='LEG4')

#forest green
x_5,y_5 = map(clon_5,clat_5)
map.scatter(x_5,y_5,4,marker='o',lw=0, c='#228b22', label='LEG5')

#coral
x_6,y_6 = map(clon_6,clat_6)
map.scatter(x_6,y_6,4,marker='o',lw=0, c='#ff7f50', label='LEG6')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4, fontsize=8, markerscale=5)

plt.title('EXAMPLE FIG')
plt.savefig('image', bbox_inches='tight',dpi=300)
