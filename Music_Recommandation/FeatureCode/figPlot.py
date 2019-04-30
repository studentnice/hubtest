#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:14:14 2019

@author: bob
"""
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import gc

def pltSave(filepath, targetpath):
    newfilepath = targetpath + '.png'
    if os.path.exists(newfilepath):
        print('Already has' + '\t')
    else:
    #print(targetpath)
        print('Figuring...' + '\t')
        y, sr = librosa.load(filepath)
        
        fig = plt.gcf()
        melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
        # convert to log scale
        logmelspec = librosa.power_to_db(melspec)
        # plot mel spectrogram
        librosa.display.specshow(logmelspec, sr=sr)
        fig.set_size_inches(25.6 ,2.56)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        plt.margins(0,0)
        fig.savefig(newfilepath, 
                    transparent=True, dpi=100, pad_inches = 0)
        plt.close()
        del y, sr, fig, melspec, logmelspec
        gc.collect()
        print(targetpath)
        print("Done")