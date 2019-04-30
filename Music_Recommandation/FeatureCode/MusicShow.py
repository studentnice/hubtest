#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:18:33 2019

@author: bob
"""

import figPlot
import numpy as np
import pandas as pd
from scipy import misc
from keras.models import Model
from keras.layers import Input, Conv2D, BatchNormalization
from keras.layers import LeakyReLU, MaxPooling2D, GlobalMaxPooling2D, Dense
import webbrowser
import os
import glob
from tqdm import tqdm
import sys

def imread(f):
    x = misc.imread(f, mode='RGB')
    return x.astype(np.float32) / 255 * 2 - 1

#create AutoEncoder
def AutoEncoder(ImgShape):
    '''
    paragrams: ImgData size is [height, weight]
    '''
    img_height = ImgShape[0]
    img_weight = ImgShape[1]

    z_dim = 128 # 隐变量维度
    
    # 编码器（卷积与最大池化）
    x_in = Input(shape=(img_height, img_weight, 3))
    x = x_in
    
    for i in range(4):
        x = Conv2D(int(z_dim / 2**(3-i)), 
                   kernel_size=(3,3), padding='SAME')(x)
        x = BatchNormalization()(x)
        x = LeakyReLU(0.2)(x)
        x = MaxPooling2D((2, 2))(x)

    for i in range(2):
        x = Conv2D(z_dim,
                   kernel_size=(3,3),
                   padding='SAME')(x)
        x = BatchNormalization()(x)
        x = LeakyReLU(0.2)(x)
    
    x = GlobalMaxPooling2D()(x) # 全局特征
    
    z_mean = Dense(z_dim)(x) # 均值，也就是最终输出的编码
    encoder = Model(x_in, z_mean) # 总的编码器就是输出z_mean
    return encoder

def calcuSimMus(zs):
    topn = 11
    idxs = ((zs**2).sum(1) + (zs[1500]**2).sum() - 2 * np.dot(zs, zs[1500])).argsort()[1:topn]
    similar_list = idxs.tolist()
    return similar_list

def getMusicName(simiList):
    Music_list = []
    img_data = pd.read_csv('../Data/nameIndex.csv', names=['id', 'name'])
    for sims in simiList:
        simImage = img_data[img_data['id']==int(sims)]
        simName = simImage['name'].values[0]
        Music_list.append(simName)
        print(simName)
    return Music_list

def srcGet(path, name):
    return path + name

def nameGet(name):
    return os.path.splitext(name)[0]

def simPer(N):
    return [str(round((N-i) / (N/10)-9, 2)*100)+'%' for i in range(1, 11)]

def main(filename):
    MusicName = filename
    
    #图片集存放路径 
    img_path = '../MusicInputFig_Eng/*' 
    imgs = glob.glob(img_path) #读取该路径下所有图片 返回路径列表list
    
    percentage = simPer(1500)
    
    #得到训练集  注意: 这步很耗内存
    img_train = []
    for imgPath in imgs[:1500]:
        img = imread(imgPath)
        img_train.append(img)
        del img
        
    MusicDir = '../testMusic/music/'
    FigDir = '../testMusic/musicFig/'
    absolutelyMusicDir = '/home/bob/Desktop/Music_Recommend/testMusic/music/'
    musicDir = '/home/bob/Music/music_dataset/'
    
    musicPath = MusicDir + MusicName
    musicFigPath = FigDir + MusicName
    FigPath = musicFigPath + '.png'
    
    figPlot.pltSave(musicPath, musicFigPath)
    
    img = imread(FigPath)
    img_train.append(img)
    
    image_train = np.array(img_train)  
    x_train = image_train
    del img_train
    
    encoder = AutoEncoder([256, 2560])
    
    musicVec = encoder.predict(x_train, verbose=True)
    #np.savetxt('/home/bob/Desktop/MusicVec.txt', zs, delimiter=',')
    simiList = calcuSimMus(musicVec)
    recMusic = getMusicName(simiList)
    
    nameHtml = '../musicShow.html'
    f = open(nameHtml, 'w')
    message = """
    <!DOCTYPE html>
    
    <!DOCTYPE >
    <html >
    
    	<style type="text/css">
    		body {
    			color: #00ffff;
    		}
    		
    		#player,
    		#list {
    			margin: 35px;
    		}
    		
    		a,
    		a:visited,
    		a:active {
    			color: #02F78E;
    			text-decoration: none;
    			font-size: 15px;
    		}
    		
    		a:hover {
    			color: #1abc9c;
    			text-decoration: none;
    		}
    		
    		#wrap {
                background-image: url(Data/timg2.jpeg);
    			Background-size: cover;
    			margin: 10px;
    			padding: 10px 10px 10px 20px;
    			width: 350px;
    			-webkit-box-shadow: 0 0 15px #000;
    			-moz-box-shadow: 0 0 15px #000;
    			box-shadow: 0 0 15px #000;
    			-webkit-backface-visibility: hidden;
    			-webkit-border-radius: 2px;
    			-moz-border-radius: 2px;
    			border-radius: 2px;
    		}
    		
    		#now,
    		#mp3name {
    			font-size:12px;
    			font-family: 宋体;
    			float: left;
    			margin: 10px;
    		}
    		
    		#title {
    			color: #80FFFF;
    			margin: 10px 10px 15px 10px;
    			font-style: italic;
    			font-weight: bold;
    			font-size:23px;
    			font-family: ;  //前三行字体
    		}
    		
    		#search {
    			margin : 10px;
    		}
    		
    		#ftitle {
    			margin-bottom: 10px;
    			padding: 0px;
    			font-size: 24px;
    			font-weight: bold;
    		}
    		
    		#stitle {
    			margin: 0px;
    			padding: 0px;
    			font-size: 20px;
    		}
    		
    	</style>
    
    	<head>
    		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    		<title>HTML5音乐播放器</title>
    		<meta name="keywords" content="HTML5音乐播放器。" />
    	</head>
    
    	<body > <!-- 背景图片-->
    		<div id="wrap">
    			<div id="list">
    				<p id="ftitle">所选歌曲</p>
    				<div id="title">
    					<a href="javascript:void(0);" onclick="playmusic(0)">%s</a>
    				</div>
    				
    				<p id="stitle">推荐歌曲</p><br />
    				
    				<form>
    				
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(1)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(2)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(3)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(4)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(5)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(6)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(7)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(8)">%s</a>
    				</li>
    				<li>
    					<a href="javascript:void(0);" onclick="playmusic(9)" >%s</a>
    				</li>
                    <li>
    					<a href="javascript:void(0);" onclick="playmusic(10)" >%s</a>
    				</li>
    			</div>
    			<audio id="player" controls="true">你的浏览器太烂了</audio>
    			<div id="now">正在播放：</div><span id="mp3name">无</span>
    			<div style="clear:both"></div>
    		</div>
    	</body>
    
    	<script type="text/javascript">
    		function playmusic(i) {
    			var my = document.getElementById("player");
    			switch(i) {
                	case 0:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 1:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 2:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 3:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 4:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 5:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 6:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 7:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 8:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				case 9:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
                    case 10:
    					my.setAttribute("src", "%s");
    					document.getElementById("mp3name").innerText = "正在获取歌曲。。。";
    					my.addEventListener("canplaythrough",
    						function() {
    							document.getElementById("mp3name").innerText = "%s";
    						}, false);
    					my.play();
    					break;
    				default:
    			}
    
    		}
    	</script>Design by Bob    
        """%(nameGet(MusicName), 
        nameGet(percentage[0]+' '+recMusic[0]), 
        nameGet(percentage[1]+' '+recMusic[1]), 
        nameGet(percentage[2]+' '+recMusic[2]), 
        nameGet(percentage[3]+' '+recMusic[3]), 
        nameGet(percentage[4]+' '+recMusic[4]), 
        nameGet(percentage[5]+' '+recMusic[5]), 
        nameGet(percentage[6]+' '+recMusic[6]), 
        nameGet(percentage[7]+' '+recMusic[7]), 
        nameGet(percentage[8]+' '+recMusic[8]), 
        nameGet(percentage[9]+' '+recMusic[9]), 
        srcGet(absolutelyMusicDir, MusicName),
        nameGet(MusicName),    
        srcGet(musicDir, recMusic[0]), 
        nameGet(recMusic[0]), 
        srcGet(musicDir, recMusic[1]), 
        nameGet(recMusic[1]), 
        srcGet(musicDir, recMusic[2]), 
        nameGet(recMusic[2]), 
        srcGet(musicDir, recMusic[3]), 
        nameGet(recMusic[3]), 
        srcGet(musicDir, recMusic[4]), 
        nameGet(recMusic[4]), 
        srcGet(musicDir, recMusic[5]), 
        nameGet(recMusic[5]), 
        srcGet(musicDir, recMusic[6]), 
        nameGet(recMusic[6]), 
        srcGet(musicDir, recMusic[7]), 
        nameGet(recMusic[7]), 
        srcGet(musicDir, recMusic[8]),
        nameGet(recMusic[8]),
        srcGet(musicDir, recMusic[9]),
        nameGet(recMusic[9])
        )
    
    
    f.write(message)
    f.close()
    
    webbrowser.open(nameHtml, new=1)
    
if __name__ == '__main__':
    main(sys.argv[1])