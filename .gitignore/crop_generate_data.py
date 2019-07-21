# Crop Training Images
import PIL.Image
import numpy as np
import os
import sys
import tarfile
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from IPython.display import display, Image, HTML
import h5py

def crop(box_data,dataset):
    imsize = np.ndarray([len(box_data),2])
    for i in np.arange(len(box_data)):
        im_path = os.path.join("data/"+dataset+"/", box_data[i]['filename'])
        im = PIL.Image.open(im_path)
        imsize[i, :] = im.size[:]
    return imsize


def building_dataset(data, folder,size_image,depth):

    dataset = np.ndarray([len(data),size_image,size_image,depth], dtype='float32')
    labels = np.ones([len(data),6], dtype=int) * 10
    for i in np.arange(len(data)):
        filename = data[i]['filename']
        fullname = os.path.join(folder, filename)
        im = PIL.Image.open(fullname)
        boxes = data[i]['boxes']
        num_digit = len(boxes)
        labels[i,0] = num_digit
        top = np.ndarray([num_digit], dtype='float32')
        left = np.ndarray([num_digit], dtype='float32')
        height = np.ndarray([num_digit], dtype='float32')
        width = np.ndarray([num_digit], dtype='float32')
        for j in np.arange(num_digit):
            if j < 5: 
                labels[i,j+1] = boxes[j]['label']
                if boxes[j]['label'] == 10: labels[i,j+1] = 0
            else: aa=1
            top[j] = boxes[j]['top']
            left[j] = boxes[j]['left']
            height[j] = boxes[j]['height']
            width[j] = boxes[j]['width']
        
        im_top = np.amin(top)
        im_left = np.amin(left)
        im_height = np.amax(top) + height[np.argmax(top)] - im_top
        im_width = np.amax(left) + width[np.argmax(left)] - im_left
        
        im_top = np.floor(im_top - 0.1 * im_height)
        im_left = np.floor(im_left - 0.1 * im_width)
        im_bottom = np.amin([np.ceil(im_top + 1.2 * im_height), im.size[1]])
        im_right = np.amin([np.ceil(im_left + 1.2 * im_width), im.size[0]])

        im = im.crop((im_left, im_top, im_right, im_bottom)).resize([size_image,size_image])
        if depth==3:
            im = (np.array(im, dtype='float32'))
        else:
            im = np.dot(np.array(im, dtype='float32'), [[0.2989],[0.5870],[0.1140]])
            mean = np.mean(im, dtype='float32')
            std = np.std(im, dtype='float32', ddof=1)
            if std < 1e-4: std = 1.
            im = (im - mean) / std
        dataset[i,:,:,:] = im[:,:,:]

    return dataset, labels

