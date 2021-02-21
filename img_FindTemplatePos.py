import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(img):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()
    


img = cv2.imread('img/IMG15.bmp',0) # Grayscale img
# print(img)
# plt.imshow(img)
# plt.show()
display_img(img)
# print(img.shape)

top_left  = [[770,530],[780,530],[780,520],[780,490],[770,460],[760,425],[750,390],[750,350],[740,320],[730,270],
        [720,230],[705,175],[690,120],[680,60],[670,0]]
bottom_right = [[810,570],[820,570],[820,560],[820,530],[810,500],[810,475],[800,440],[800,400],[790,370],[780,320],
        [770,280],[760,230],[750,180],[740,120],[730,60]]