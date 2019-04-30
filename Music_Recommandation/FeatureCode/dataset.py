import numpy as np
import pandas as pd
import glob
import imageio
from scipy import misc
from keras.models import Model
from keras.layers import *
from keras import backend as K
from keras.optimizers import Adam
import csv
from tqdm import tqdm
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
#%matplotlib inline

#图片集存放路径 
img_path = '../MusicInputFig/*' 
imgs = glob.glob(img_path) #读取该路径下所有图片 返回路径列表list

def imread(f):
    x = misc.imread(f, mode='RGB')
    return x.astype(np.float32) / 255 * 2 - 1

def Imgdataset():
	#得到训练集  注意: 这步很耗内存
	img_train = []
	index = 0
	with open('../Data/nameIndex.csv', 'w') as csv_file:
	    writer = csv.writer(csv_file)
	    for imgPath in tqdm(iter(imgs[:2000])):
	        fname = os.path.splitext(imgPath.split('/')[-1])[0] #获得歌曲名
	        row = [index, fname]
	        writer.writerow(row)
	        index = index+1
	        
	        img_train.append(imread(imgPath))

	image_train = np.array(img_train)  
	x_train = image_train
	del img_train
	return x_train