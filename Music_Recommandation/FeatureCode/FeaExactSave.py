#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:30:53 2019

@author: bob
"""

import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np 
import time
#from PIL import Image
import os

#import py_file_model
import Music_suffix 
import Music_namelist

#get music suffix of all 
suffix = Music_suffix.suffixList() 
#music_dir = '/home/bob/Music/CloudMusic/'
music_dir = '/media/bob/LocalDisk/CloudMusic/'
musicInfo_path = '../MusicInfo/'

#get the names of all music with suffix in the music_dir
music_list = Music_namelist.nameList(music_dir, suffix)  

def splitName(name):
    folder = name.split('.')[0].strip(' ')
    return folder

def FeaExtra(y, sr):
    #chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    #chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)

    melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    rmse = librosa.feature.rmse(y=y)

    S = np.abs(librosa.stft(y))
    spectral_contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
    #从音频时间序列中提取谐波元素
    y_hrmonic = librosa.effects.harmonic(y)
    tonnetz = librosa.feature.tonnetz(y=y_hrmonic, sr=sr)

    logmelspec = librosa.power_to_db(melspectrogram)

    #spectral_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    #spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)

    #often converted to dB scale.
    #spectral_flatness = librosa.feature.spectral_flatness(y=y)
    #spectral_rolloff = librosa.feature.spectral_rolloff(y=y,sr=sr, roll_percent=0.95)

    #获得将n阶多项式拟合到谱图列的系数
    #p0 = librosa.feature.poly_features(S=S, order=0)
    #p1 = librosa.feature.poly_features(S=S, order=1) #线性拟合
    #p2 = librosa.feature.poly_features(S=S, order=2) #平方拟合

    #zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

    #节拍跟踪器, 返回每分钟估计节拍数量 和 检测到节奏的帧数位置的列表
    #tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    features = [chroma_cens, 
               melspectrogram,
               mfcc,
               rmse,
               spectral_contrast,
               tonnetz,
               logmelspec]
    return features

def chromaSave(feature, feature_name, savePath):
    plt.figure(figsize=(100, 10))
    librosa.display.specshow(feature)
    #feature_name = str(feature)
    filepath = savePath + '/' +  feature_name + '.png'
    #print(filepath)
    plt.savefig(filepath, dpi=128, 
            transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()
    
def hzSave(feature, feature_name, savePath):
    plt.figure(figsize=(100, 10))
    librosa.display.specshow(librosa.power_to_db(feature,ref=np.max), 
                         fmax=8000)
    #feature_name = str(feature)
    filepath = savePath + '/' + feature_name + '.png'
    plt.savefig(filepath, dpi=128, 
            transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()

def PlotAndSave(features, newTargetPath):
    chroma_cens, melspectrogram,mfcc,rmse,spectral_contrast,tonnetz,\
        logmelspec = features
    chromaSave(chroma_cens, 'chroma_cens', newTargetPath)
    hzSave(melspectrogram, 'melspectrogram', newTargetPath)
    chromaSave(mfcc, 'mfcc', newTargetPath)
    chromaSave(spectral_contrast, 'spectral_contrast', newTargetPath)
    chromaSave(tonnetz, 'tonnetz', newTargetPath)
    chromaSave(logmelspec, 'logmelspec', newTargetPath)

import gc   

number_all = len(music_list)
done = 0
for name in music_list:
    done += 1
    filepath = music_dir + name
    targetpath = musicInfo_path + splitName(name).replace(' ', '')
    try:
        os.mkdir(targetpath)
        newTargetPath = targetpath + '/'
        #load music
        y, sr = librosa.load(filepath)
        #print("Loading... Done")
        #get feature
        features = FeaExtra(y, sr)
        #print("Feature... Done")
        #plot and Save
        PlotAndSave(features, targetpath)
        #show percentage
        print("runing :{0}%".format(round((done + 1) * 100 / number_all)), end="\r")
        time.sleep(0.01)
        del y
        del sr
        del features
        gc.collect() 
        #print(newTargetPath)
    except FileExistsError or NoBackendError:
        continue
"""
music_info_path = '../MusicInfo/'
filepath = '/home/bob/Music/CloudMusic/test.mp3'

#load music
y, sr = librosa.load(filepath)

#---------------------Feature Extraction----------------------

#chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
#chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)
chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
rmse = librosa.feature.rmse(y=y)
S = np.abs(librosa.stft(y))
spectral_contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
#从音频时间序列中提取谐波元素
y_hrmonic = librosa.effects.harmonic(y)
tonnetz = librosa.feature.tonnetz(y=y_hrmonic, sr=sr)
logmelspec = librosa.power_to_db(melspectrogram)
#spectral_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
#spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
#often converted to dB scale.
#spectral_flatness = librosa.feature.spectral_flatness(y=y)
#spectral_rolloff = librosa.feature.spectral_rolloff(y=y,sr=sr, roll_percent=0.95)
#获得将n阶多项式拟合到谱图列的系数
#p0 = librosa.feature.poly_features(S=S, order=0)
#p1 = librosa.feature.poly_features(S=S, order=1) #线性拟合
#p2 = librosa.feature.poly_features(S=S, order=2) #平方拟合
#zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
#节拍跟踪器, 返回每分钟估计节拍数量 和 检测到节奏的帧数位置的列表
#tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

#----------------------Done------------------------------

#------------------------Plot and Save-------------------------
#chromaSave(chroma_cens, 'chroma_cens')
hzSave(melspectrogram, 'melspectrogram')
#chromaSave(mfcc, 'mfcc')
#chromaSave(spectral_contrast, 'spectral_contrast')
#chromaSave(tonnetz, 'tonnetz')
#chromaSave(logmelspec, 'logmelspec')
#------------------------Done--------------------------
"""