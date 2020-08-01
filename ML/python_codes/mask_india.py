import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import cartopy
fname = './state_shp/Admin2.shp' #insert path
import numpy as np
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import xarray as xr

xf=xr.open_dataset("./data/files.nc")
data=xf["IMG_TIR1"]

fig = plt.figure()

ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([44.5, 105.5, -10, 45], crs=ccrs.PlateCarree())


ax.coastlines(resolution='10m', color='white', linewidth=0.4)

ax.gridlines(color='white', alpha=0.5, linestyle='--', linewidth=0.4)

arr=data[0].values

shapefile = list(shpreader.Reader(fname).geometries())



img=ax.imshow(arr,cmap="gray",extent=[44.5, 105.5, -10, 45],)#transform=ccrs.Mercator())

ax.add_geometries(shapefile, crs=ccrs.PlateCarree(), facecolor='none', edgecolor='white',linewidth=0.4)
# plt.tight_layout()
# plt.colorbar(img, label='Temperatures (K)', extend='both', orientation='vertical', pad=0.05, fraction=0.05)
plt.show()


# plt.savefig("draw.png",transparent = True, bbox_inches = 'tight', pad_inches = 0, dpi=400,format="png",figsize=(10,12))


