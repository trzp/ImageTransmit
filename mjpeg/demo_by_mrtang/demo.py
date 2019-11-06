#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/19 14:45
# @Version : 1.0
# @File    : demo.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved


from mjpeg.client import MJPEGClient
import cv2
import numpy as np
import pygame


url = 'http://192.168.1.1:8080/?action=stream'

# Create a new client thread
client = MJPEGClient(url)

# Allocate memory buffers for frames
bufs = client.request_buffers(65536, 50)
for b in bufs:
    client.enqueue_buffer(b)
# Start the client in a background thread
client.start()

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)


while True:
    buf = client.dequeue_buffer()

    im = cv2.imdecode(np.array(buf.data),cv2.IMREAD_COLOR)
    imm = im[:,:,::-1]
    pgsur = pygame.image.fromstring(imm.flatten().tostring(np.uint8),(320,240),'RGB')
    screen.blit(pgsur, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        pass

    # cv2.imshow('ii',im)
    # cv2.waitKey(20)
    # <do some work>
    client.enqueue_buffer(buf)


