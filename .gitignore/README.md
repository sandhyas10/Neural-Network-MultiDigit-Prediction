The goal of the project is to model a network to recogninze multidigits in Street View Images. This project is inspired by the paper Multi-digit Number Recognition from Street View Imagery using Deep Convolutional Neural Networks (Goodfellow et al. 2014)

Following are the packages to be installed:

h5py
``` 
pip install h5py
```

#### Data Collection:

Data\_prepocessing.ipynb contains the code to import the format1 images from the [link](http://ufldl.stanford.edu/housenumbers/) and preprocessing. The dataset consists of train, test and extra. Since extra dataset size is huge we have shown the image processing for the train and test set that include downloading the tar file, extracting images, getting boundaries of images to be cropped and creating a train, test and validation set.
The code allows one to get the dataset in any form- varying image size (eg: 32,64) or varying depths (eg: grayscale=1, rgb=3)
The notebool is commented on how to obtain the data required.

#### Models:

Different Models are tried exploring various optimization techniques, types of normalization, size of images, digit length, no. of layers to find effective methodoogies to build a Convolutional Neural Network

- 7-layer_model_ss5116_kc3507.ipynb	: Implements a 7-layer ConvNet model    
- 8-layer_5-digit_ss5116_kc3507.ipynb	: Implements a 8-layer ConvNet model which predicts 5-digit numbers or lesser   
- 8-layer_model_54X54_ss5116_kc3507.ipynb : Implements a 8-layer ConvNet model of image size 54 x 54   
- 8-layer_model_6digits_ss5116_kc3507.ipynb	: Implements a 8-layer ConvNet model which predicts 6-digit numbers or lesser     
- Batch_Normalization_ss5116_kc3507.ipynb : Implements a ConvNet model using Batch Normalization 	    
- CNN+with+Local+Response+Normalization-Adam+Optimizer_ss5116_kc3507.ipynb	: Implements a ConvNet model using Local Response Normalization and Adam Optimizer   
- CNN_with_Local_Response_Normalization-AdaGrad_ss5116_kc3507.ipynb	: Implements a ConvNet model using Local Response Normalization and AdaGrad Optimizer   
- CNN_with_Local_Response_Normalization_ss5116_kc3057.ipynb	: Implements a ConvNet model using Local Response Normalization and RMSProp Optimizer    
- No_Normalization-RMS_prop_ss5116_kc3057.ipynb	: Implements a ConvNet model with no Normalization and RMSProp Optimizer



.


