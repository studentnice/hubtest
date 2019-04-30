import glob 
import os 
import shutil                                                           

def getSuf(src): 
    suffix = [] 
    files = glob.glob(src+'*') 
    for names in files: 
        suf = os.path.splitext(names)[-1] 
        if suf not in suffix: 
            suffix.append(suf) 
    return suffix 
                                                                        

src = '/media/bob/LocalDisk/CloudMusic/' #源文件地址  
dst = '/home/bob/Music/Eng_music_dataset/' #目的文件地址 
suffix_list = getSuf(src) #目的文件后缀列表                             

suffix_list.remove('') 
suffix_list.remove('.ncm') 
suffix_list.remove('.jpg') 

for suffix in suffix_list: #遍历每一个后缀
    src_path = os.path.join(src, '*'+suffix) #获得当前目录下所有后缀文件的路径
    music_kinds = glob.glob(src_path) #获得当前目录下所有后缀文件
    for music_path in music_kinds: #得到此后缀名所欲文件路径
        music_name = os.path.split(music_path)[-1] #获得文件名
        target_name = dst + music_name
        shutil.copyfile(music_path, target_name)
        print(target_name)
