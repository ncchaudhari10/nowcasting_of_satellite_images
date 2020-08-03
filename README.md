# NM374_Apollo6
###### This repo has implemented Nowcasting of Meteorological Satellite Images of INSAT-3D and INSAT-3DR for next 3 hrs at an interval of 30 min using AI/ML techniques.
###### A composite model containing encoding, decoding and forecasting module which are formed by stacking several ConvLSTM layers.
###### Initial states of the decoding and forecasting module are copied from the last state of the encoding module. Encoding-Forecasting model will take 6 present images as input to predict 6 future images as output.
###### Repo also has the implementation of Software solution. Flask web framework is used to encapsulate the model to provide dynamic results.

## Dependencies and installations:
  * Python 3.6+
  * Flask `pip install flask`
  * Numpy `pip install numpy`
  * Pandas `pip install pandas`
  * H5py `pip install h5py`
  * xarray `pip install xarray`
  * tensorflow-gpu==2.2.0 `as this version is not available for pip, kindly use google collab for training the models`

## Model Architecture:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## Website portal for the Visualization:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## Results:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

##### Error calculation between 1st and 2nd predicted frame
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## Validation of prediction on 18th May '20 and 25th July '20 Data
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
