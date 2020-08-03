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
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/model.png)

## Website portal for the Visualization:
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/webportal.png)

## Train:
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/edit/master/README.md)

## Results:
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/resultTIR13D.png)

### Difference in 1st Ground Truth and 1st Predicted frame
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/errorcal.png)

![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/errorplot_resultTIR13D.png)

![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/correlationtir1.png)
![alt text](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/ROC25july.png)
![alt-text-1](https://github.com/dr3aMer10/NM374_Apollo6/blob/master/readme_imgs/validation_insat3d_TIR.png)

