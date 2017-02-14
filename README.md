# nbviewerlike
## 服务器方式 - 像nbviewer一样，提供web界面并调度容器
## 独立使用容器
1、docker pull yejinlei/nbviewerlike #下载镜像
2、docker run --rm --net=host yejinlei/nbviewerlike python /root/containermain.py 8888 'create'   #创建临时笔记
3、docker run --rm --net=host yejinlei/nbviewerlike python /root/containermain.py 8888 'download' yejinlei about-python #抓取https://github.com/yejinlei/about-python
