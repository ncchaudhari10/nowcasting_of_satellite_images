import xarray as xr 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

xf=xr.open_dataset("files_3dr.nc")

tir1=xf["IMG_TIR1"][:100].values
tir2=xf["IMG_TIR2"][:100].values
wv=xf["IMG_WV"][:100].values
mir=xf["IMG_MIR"][:100].values

vis=xf["IMG_VIS"][:100].values

def correlate(rf,rf1):
   crf=[]
   a=rf.shape[0]
   print(rf1.shape)
   print(rf.shape)  
   for z in range(a):
   
      h=np.corrcoef(rf[z,:], rf1[z,:],rowvar=True)
      v=h[1,0]
      crf.append(v)
      
   return crf
   
def mse(rf,rf1):
   mse=[]
   a=rf.shape[0]
   print(rf1.shape)
   print(rf.shape)  
   for z in range(a):
   
      h=mean_squared_error(rf[z,:],rf1[z,:])
      mse.append(h)
      
   return mse

tir1=tir1.reshape((-1,404*404))
vis=vis.reshape((-1,404*404))
tir2=tir2.reshape((-1,404*404))
mir=mir.reshape((-1,404*404))
wv=wv.reshape((-1,404*404))

h=np.corrcoef(tir1,vis,rowvar=True)
v=h[1,0]
print(v)

h=np.corrcoef(tir2,vis,rowvar=True)
v=h[1,0]
print(v)
h=np.corrcoef(mir,vis,rowvar=True)
v=h[1,0]
print(v)
h=np.corrcoef(wv,vis,rowvar=True)
v=h[1,0]
print(v)

Z=correlate(vis,tir1)
C=correlate(vis,tir2)
X=correlate(vis,wv)
D=correlate(vis,mir)

# bin=np.arange(0,0.9,0.01)

sns.distplot(Z, hist=False, kde=True, 
             bins = bin, color = 'red',label = 'TIR1',
             kde_kws={'linewidth': 4})

sns.distplot(C, hist=False, kde=True, 
             bins = bin, color = 'green',label = 'TIR2', 
             kde_kws={'linewidth': 4})

sns.distplot(X, hist=False, kde=True, 
             bins = bin, color = 'blue',label = 'Water Vapour',
             kde_kws={'linewidth': 4})
             
sns.distplot(D, hist=False, kde=True, 
             bins = bin, color = 'black',label = 'MIR',
             kde_kws={'linewidth': 4})
plt.legend()
plt.xlabel('CORRELATION', fontsize=21)
plt.ylabel('PDF',fontsize=21)

ax=plt.gca()
ax.set_facecolor((0.73,0.73,0.73))
ax.tick_params(labelsize='x-large')
plt.tight_layout()
plt.savefig('Correlation_3DR.png',dpi=400,format='png')

plt.close()