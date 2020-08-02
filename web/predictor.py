
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

import xarray as xr 

def scaleData(a):       
    return (a-np.nanmin(a))/(np.nanmax(a)-np.nanmin(a))

def prepare_data(data):
    tdata=[]
    tlabels=[]
    img_size=(404,404)
    print(len(data))
    arrdata=np.ones((len(data)-6,6,img_size[0],img_size[1],1))
    arrlabel=np.ones((len(data)-6,6,img_size[0],img_size[1],1))
    
    for i in range(0,len(data)-6-5,1):
        m=0
        for j in range(i,i+6,1):

            arrdata[i,m,:,:,0]=data[j]
            arrlabel[i,m,:,:,0]=data[j+6] 

            m+=1
        # print(i,j,j+1,j+6)

    print(arrdata.shape)
    print(arrlabel.shape)
    return arrdata,arrlabel


def predict(x, encoder_predict_model, decoder_predict_model, num_steps_to_predict):
  
    y_predicted = []
    
    state_h,state_c = encoder_predict_model.predict(x)
    states=[state_h,state_c]    
    decoder_input = np.zeros((1,1,404,404,1))
    decoder_input[0,0,:,:,0]=x[0,-1,:,:,0]
    
    for _ in range(num_steps_to_predict):
        outputs_and_states = decoder_predict_model.predict([decoder_input] + states)
      
        output = outputs_and_states[0]
      
        states= outputs_and_states[1:]
       

        # add predicted value
        output=scaleData(output)
        decoder_input=output

        y_predicted.append(output)
    return np.concatenate(y_predicted, axis=1)

def predict_(x, encoder_predict_model, decoder_predict_model, num_steps_to_predict):
  
    y_predicted = []
    
    state_h,state_c = encoder_predict_model.predict(x)
    states=[state_h,state_c]    
    decoder_input = np.zeros((1,1,404,404,1))
    # decoder_input[0,0,:,:,0]=x[0,-1,:,:,0]
    
    for _ in range(num_steps_to_predict):
        outputs_and_states = decoder_predict_model.predict([decoder_input] + states)
      
        output = outputs_and_states[0]
      
        states= outputs_and_states[1:]
       
        # add predicted value
        # output=scaleData(output)
        decoder_input=output

        y_predicted.append(output)
    return np.concatenate(y_predicted, axis=1)

def predictorsih():
  xf=xr.open_dataset("uploadedData/files.nc")

  data=xf["IMG_TIR1"].values
  xf.close()
  new=[]
  for i in data:
      value=scaleData(i)
      new.append(value)

  data,label=prepare_data(new[101:140])


  Encoder_model=load_model("models/INSAT-3D/TIR1/Encoder.h5")
  Decoder_model=load_model("models/INSAT-3D/TIR1/Decoder.h5")
  Forecaster_model=load_model("models/INSAT-3D/TIR1/Forecaster.h5")
 
  directory="static/predictedImages/"
  print("done")
 
#   C:\Users\vpras\OneDrive\Desktop\New folder (2)\ojaswi\trial-working (1)\trial-working\
#       C:\Users\vpras\OneDrive\Desktop\New folder (2)\ojaswi\trial-working (1)\trial-working\models\INSAT-3D\MIR\Forecaster_MIR.h5


  var=24 #we 25set of images in validation set var =1(six set of input images )
  channel_name="TIR2"#channel name you like to save by name
  ans= predict( data[var,np.newaxis], Encoder_model, Forecaster_model, 12)


  ans1= predict_( data[var,np.newaxis], Encoder_model, Decoder_model, 6)
  ans1[:,:,:,:,:]=ans1[:,::-1,:,:,:]
  channel_name="TIR1"
  print("DONE WITH upload")

  for i in range(6):
    print("secondloop")
    plt.imshow(data[var,i,:,:,0],cmap="gray",vmin=0,vmax=1)
    plt.title(channel_name+str(var)+str(i),fontweight ="bold") 
    plt.imsave(directory+"seq"+str(i+1)+".png",arr=ans[0,i,:,:,0],cmap="gray")

