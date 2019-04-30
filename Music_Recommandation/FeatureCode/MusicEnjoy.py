# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import webbrowser
import os
import Music_Recommend
import numpy as np
import sys

musicDir = '/home/bob/Music/music_dataset/'
'''
music_dic = {
        'Anthem Lights - Love You Like the Movies.mp3':
           ['Blue Stahli - Suit Up.mp3', 
            'Corporate - Scandal.mp3', 
            'Cryptex - Antique Gucci (Cryptex Mashup).mp3', 
            'G.E.M.邓紫棋 - 我的秘密.mp3', 
            'Hyper Potions - Christmas Morning.mp3', 
            'Kory Burns - Count the Ways (Main Mix).mp3', 
            "Matt Beilis - We've Been Here Before.mp3",
            "Stepcat - Jitterbug.mp3", 
            "Stepcat - Jitterbug.mp3"]}
'''

def srcGet(path, name):
    return path + name

def nameGet(name):
    return os.path.splitext(name)[0]

def simPer(N):
    return [str(round((N-i) / (N/10)-9, 2)*100)+'%' for i in range(1, 11)]

def main():
    if len(sys.argv) >= 2:
        music_dic = Music_Recommend.MusicDicGet(musicIndex=int(sys.argv[1]))
    else:
        music_dic = Music_Recommend.MusicDicGet()
    music_index = np.random.choice(len(music_dic.keys())) #音乐编号 #随机选取推荐n个中的一个
    tarMusic = list(music_dic.keys())[music_index] #获得音乐字典 keys 中第一个键变量
    recMusic = list(music_dic.values())[music_index]
    percentage = simPer(1500)
    
    
    
    nameHtml = '../musicEnjoy.html'
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
        """%(nameGet(tarMusic), 
        nameGet(percentage[0]+'\t'+recMusic[0]), 
        nameGet(percentage[1]+' '+recMusic[1]), 
        nameGet(percentage[2]+' '+recMusic[2]), 
        nameGet(percentage[3]+' '+recMusic[3]), 
        nameGet(percentage[4]+' '+recMusic[4]), 
        nameGet(percentage[5]+' '+recMusic[5]), 
        nameGet(percentage[6]+' '+recMusic[6]), 
        nameGet(percentage[7]+' '+recMusic[7]), 
        nameGet(percentage[8]+' '+recMusic[8]), 
        nameGet(percentage[9]+' '+recMusic[9]), 
        srcGet(musicDir, tarMusic),
        nameGet(tarMusic),    
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
    main()