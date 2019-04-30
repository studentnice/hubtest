#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:59:40 2019

@author: bob
"""

from os import listdir
from PIL import Image
import os

def FolderNames(path):
    '''
    path: send the target dir to this function and get all names
    return: a list of all the absolute path of each file 
    '''
    filePath = []
    for name in listdir(path):
        absPath = path + name
        filePath.append(absPath)
    return filePath

def Merge(ims, path, name):
    width, height = ims[0].size
    figout = Image.new(ims[0].mode, (width, height*len(ims)))
    for i, im in enumerate(ims):
        figout.paste(im, box=(0, i*height), )
    output_name = name + '.png'
    outPut_path = path + output_name
    figout.save(outPut_path)
    return outPut_path
    
path = '/home/bob/Desktop/Music_Recommended/MusicInfo/'
targetPath = '/home/bob/Desktop/Music_Recommended/MusicInputFig/'
#targetPath = '/home/bob/Desktop/MusicInputFig/'
#path = '/home/bob/Desktop/pic/'
#target_dir = FolderNames(path)

count = -1
file_sum = float(len(listdir(path)))
for fileDir, e , files in os.walk(path):
    if count == -1:
        count += 1
        continue
    else:
        musicName = fileDir.split('/')[-1]
        ims = []
        folderDir = fileDir + '/'
        for name in files:
            filePath = folderDir + name
            ims.append(Image.open(filePath))
        #print(ims)
        
        for name in files:
            filePath = folderDir + name
            os.remove(filePath)
        
        outcome = Merge(ims, targetPath, musicName)
        count += 1
        percentage = count/file_sum * 100
        print("{:.2f}%".format(percentage))