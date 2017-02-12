FROM ubuntu:15.04

MAINTAINER yejinlei <4010896@qq.com>

#support chinese
RUN locale-gen zh_CN.UTF-8
ENV LANG zh_CN.UTF-8
ENV LANGAGE zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8

RUN cp /etc/apt/sources.list /etc/apt/sources.listbak
COPY /etc/apt/sources.list /etc/apt/sources.list
COPY fetch.py /root/fetch.py
RUN chmod 777 fetch.py
COPY containermain.py /root/containermain.py
RUN chmod 777 containermain.py

RUN echo "deb http://mirrors.163.com/ubuntu/ vivid main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ vivid-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ vivid-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ vivid-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ vivid-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ vivid main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ vivid-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ vivid-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ vivid-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ vivid-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -qq -y python2.7 python2.7-dev python-pip
RUN apt-get install git

RUN pip install --upgrade pip
RUN pip install jupyter

RUN apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/list/*
