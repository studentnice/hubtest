#!/usr/bin/env python
# coding: utf-8


#import py_file_model
import Music_suffix 
import Music_namelist

#get music suffix of all 
suffix = Music_suffix.suffixList() 
music_dir = '/home/bob/Music/CloudMusic/'

#get the names of all music with suffix in the music_dir
music_list = Music_namelist.nameList(music_dir, suffix)    

for name in music_list:
    filepath = music_dir + name
    print(filepath)



