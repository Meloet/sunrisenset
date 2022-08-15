
from fileinput import filename
from tkinter import Frame
from turtle import width
import cv2
import os
path='PRO-105-Reference-Code-Student-Activity-main/Images'
allimages=os.listdir(path)
images=[]
for image in allimages:
    filenames=path+'/'+image
    images.append(filenames)
frame=cv2.imread(images[0])
height, width,channels=frame.shape
size=(width,height)
newVideo=cv2.VideoWriter('Sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in reversed(images):
    frame=cv2.imread(i)
    newVideo.write(frame)
newVideo.release()