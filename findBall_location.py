import cv2
import numpy as np

# Initiate parameter
FL = 8
res_w = 1024
res_h = 1280
pixel_size = 0.0048
dist = 4
tilt_angle = 10*np.pi/180
rad_bb = 37.3

# Calculate working distance
wd = dist/np.cos(tilt_angle)

# Calculate diameter of object
d_bb = r_bb*2

# Calculate cx and cy (principal point of image center)
cx = 1024/2
cy = 1280/2

# Calculate sensor width and height
sensor_w = res_w * pixel_size
sensor_h = res_h * pixel_size

# Calculate fx and fy
fx = FL*res_w/sensor_w
fy = FL*res_h/sensor_h


fps = 240

