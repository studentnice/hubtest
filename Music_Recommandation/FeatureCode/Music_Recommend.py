#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:33:19 2019

@author: bob
"""

import numpy as np 
import pandas as pd

musicVec = np.loadtxt('../Data/MusicVec.txt', delimiter=',')
musicdir = '/home/bob/Music/music_dataset'

def chooseSimMus(zs, musicIndex):
    n = 1
    topn = 11
    #figure1 = np.zeros((img_height*n, img_weight*topn, 3))
    #figure2 = np.zeros((img_height*n, img_weight*topn, 3))
    #zs_ = zs / (zs**2).sum(1, keepdims=True)**0.5
    one = musicIndex
    similar_list = []
    for i in range(n):
        #one = np.random.choice(len(zs)) #随机选择一张图的序号
        idxs = ((zs**2).sum(1) + (zs[one]**2).sum() - 2 * np.dot(zs, zs[one])).argsort()[:topn] #L2 distance
        #idxs = np.dot(zs_, zs_[one]).argsort()[-topn:] # cos distance
        similar = [one, idxs.tolist()]
        similar_list.append(similar)
    return similar_list

def randomSimMus(zs):
    #musInputList = [236, 344, 407, 426, 744, 214, 1977, 1675, 1535, 1371]
    n = 1
    topn = 11
    #figure1 = np.zeros((img_height*n, img_weight*topn, 3))
    #figure2 = np.zeros((img_height*n, img_weight*topn, 3))
    #zs_ = zs / (zs**2).sum(1, keepdims=True)**0.5
    similar_list = []
    for i in range(n):
        one = np.random.choice(len(zs)) #随机选择一张图的序号
        idxs = ((zs**2).sum(1) + (zs[one]**2).sum() - 2 * np.dot(zs, zs[one])).argsort()[:topn] #L2 distance
        #idxs = np.dot(zs_, zs_[one]).argsort()[-topn:] # cos distance
        similar = [one, idxs.tolist()]
        similar_list.append(similar)
    return similar_list

def MusicDicGet(**kwargs):
    try:
        similar_list = chooseSimMus(musicVec, kwargs['musicIndex'])
    except KeyError:
        similar_list = randomSimMus(musicVec)
    similar_dic = {}
    for img_id, name_list in similar_list:
        similar_dic[img_id] = name_list
    #similar_dic
    
    similar_arr = pd.DataFrame(similar_dic)
    
    similar_arr.to_csv('../Data/SimilaryMusicIndex.csv', index=False)
    #similar_arr
    
    img_ind_data = pd.read_csv('../Data/SimilaryMusicIndex.csv')
    tarImgs = img_ind_data.columns.tolist()
    img_data = pd.read_csv('../Data/nameIndex.csv', names=['id', 'name'])
    #img_data.head()
    
    Music_dic = {}
    
    for img_id in tarImgs:
        targetImg = img_data[img_data['id']==int(img_id)]
        targetImgName = targetImg['name'].values[0]
        simImgs = img_ind_data[img_id].values.tolist()
        print("Input Image name is:"+'\n', '\t' + targetImgName)
        print('Similar Image name is:')
        Music_dic[targetImgName] = []
        for sims in simImgs:
            #print(sims)
            simImage = img_data[img_data['id']==int(sims)]
            simName = simImage['name'].values[0]
            Music_dic[targetImgName].append(simName)
            #print('\t' + os.path.join(musicdir, simName))
            print('\t' + simName)
        print('\n')
    #print(targetImgName)
    try:
        Music_dic[targetImgName].remove(targetImgName)
    except:
        pass
    return Music_dic
