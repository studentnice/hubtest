#!/usr/bin/env python
# coding: utf-8

#from PIL import Image
import time
#import py_file_model
import Music_suffix 
import Music_namelist
import figPlot

#get music suffix of all 
suffix = Music_suffix.suffixList() 
#suffix = ['.m4a']

#music_dir = '/home/bob/Music/CloudMusic/'
#music_dir = '/media/bob/LocalDisk/CloudMusic/'
music_dir = '/home/bob/Music/music_dataset/'
musicInfo_path = '../MusicInputFig/'

#get the names of all music with suffix in the music_dir
music_list = Music_namelist.nameList(music_dir, suffix)    


def Process(count, target_numb):
    print('\t' + "running: {0}% ".format(round((count + 1) * 100 / float(target_numb),3)), end="\r")
    time.sleep(0.01)

def main():
    number_all = len(music_list)
    done = 0
    for name in music_list[:]:
        try:
            done += 1
            sourcefilepath = music_dir + name #source filepath of music
            #musicName = os.path.splitext(name)[0] #filename
            #os.path.splitxext(filename) get file name and suffix
            targetpath = musicInfo_path + name
            
            #y, sr = librosa.load(filepath)
            #os.mkdir(targetpath)
            #newTargetPath = targetpath + '/' #生成新保存文件夹路径
            
            #print(musicName, newTargetPath)
    
            figPlot.pltSave(sourcefilepath, targetpath)
            #print(musicName)
    
            #show percentage
            Process(done, number_all)
        except:
            print(name)

if __name__ == '__main__':
    main()