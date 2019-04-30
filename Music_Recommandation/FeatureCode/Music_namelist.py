#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:23:49 2019

@author: bob
"""
import os
from os import listdir

'''
input:  1. music path
        2. a list contains the suffix of music needed
return: a list with the name of all music on this path 
'''
def nameList(music_dir, suffix_list):
    music_all_list = listdir(music_dir) #get names of all music in Music_dir
    music_list = []
    for name in music_all_list:
        suff = os.path.splitext(name)[-1] # get suffix of each name
        if suff in suffix_list:
            music_list.append(name)
        else:
            pass
    return music_list