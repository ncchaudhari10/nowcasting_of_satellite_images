import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


df= pd.read_csv("IMG_VIS.csv")

print(df.head())

loss=df["loss"].values
val_loss=df["val_loss"].values

fig, ax = plt.subplots()

plt.plot(loss)
plt.plot(val_loss)
plt.ylabel('Loss',fontsize=15)
plt.xlabel('Epochs',fontsize=15)
plt.legend(['loss','Val_loss'], loc='upper right',fontsize=14)
plt.title('Loss vs Epoch Graph',fontsize=17)

ax=plt.gca()

ax.set_facecolor((0.73,0.73,0.73))
ax.tick_params(labelsize='x-large')
plt.tight_layout()
plt.savefig('loss_vs_epoch.png',dpi=400,format ='png' )