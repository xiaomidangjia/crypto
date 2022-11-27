#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 22:36:16 2022

@author: carson
"""


import os
import gevent.monkey

gevent.monkey.patch_all()
import multiprocessing
#debug = True
#loglevel = 'debug'
bind = "0.0.0.0:80"
#daemon = True开启后台运行
daemon = False
timeout = 300
errorlog = '-'
accesslog = '-'
#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
x_forwarded_for_header = 'X-FORWARDED-FOR'