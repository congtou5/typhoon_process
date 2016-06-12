import netCDF4 as nc
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

obj = nc.Dataset('F:\\TyphoondataProc\\NCEPuvwind\\CFSR\\datafiles\\wnd10m.cdas1.201211.grb2.nc')
# print(obj.variables.keys())
# odict_keys(['time', 'valid_date_time', 'ref_date_time', 'forecast_hour', 'lat', 'lon', 'U_GRD_L103', 'V_GRD_L103'])

# print(obj.variables['lat'])
# valid_range: [ 15.02555084  49.98295212], current shape = (172,)
lat = obj.variables['lat'][::5]
# print(obj.variables['lon'])
# valid_range: [ 110.04545593  139.90908813], current shape = (147,)
lon = obj.variables['lon'][::5]

# print(obj.variables['U_GRD_L103'])
# level: Specified height above ground - value: 10 m, current shape = (120, 172, 147)
u = obj.variables['U_GRD_L103'][88, ::5, ::5]
v = obj.variables['V_GRD_L103'][88, ::5, ::5]


fig = plt.figure()
ax = fig.add_subplot(111)

m = Basemap(projection='cyl', llcrnrlat=20, urcrnrlat=50, llcrnrlon=105, urcrnrlon=136, resolution='l')
lons, lats = np.meshgrid(lon,lat)
# lats = lats[::-1]
m.drawparallels(np.arange(20., 46., 5.), labels=[1, 0, 0, 0], fontsize=15)
m.drawmeridians(np.arange(105., 136., 5.), labels=[0, 0, 0, 1], fontsize=15)
# m.readshapefile('E:\\shp_map\\bou2_4p','bou2_4p.shp',linewidth=1,drawbounds=True,color='gray')
m.readshapefile('F:\\TyphoondataProc\\gshhg\\coastlineOfChina_shore', 'coastlineOfChina_shore.shp', linewidth=0.5,
                drawbounds=True, color='k')
m.drawlsmask(land_color="coral", ocean_color="aqua")
# m.fillcontinents(color='coral',lake_color='aqua')
# curve=m.contour(lons,lats,u,colors='k')
# shade=m.contourf(lons,lats,u)
# m.colorbar(shade)
# plt.clabel(curve,fmt='%1.0f')
# print help(plt.quiver)

wind = m.quiver(lons, lats, u, v, width=0.002, headwidth=3, headlength=3)
plt.quiverkey(wind, 0.08, 0.95, 15, '15m/s', labelpos='S', fontproperties={'weight': 'bold'})

plt.title(u'COLD WAVE in Nov. 2012', size=20)
plt.show()
fig.savefig('quiver.png',dpi=600)
