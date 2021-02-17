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
fps = 240

# Calculate working distance
wd = dist/np.cos(tilt_angle)

# Calculate diameter of object
diameter_bb = rad_bb*2

# Calculate cx and cy (principal point of image center)
# cx = 1024/2
# cy = 1280/2

# Calculate sensor width and height
sensor_w = res_w * pixel_size
sensor_h = res_h * pixel_size

# Calculate fx and fy
# fx = FL*res_w/sensor_w
# fy = FL*res_h/sensor_h

# Calculate angle of view and field of view for this specific camera
AoV_H = 2*np.arctan(sensor_h/(2*FL)) # rad
AoV_W = 2*np.arctan(sensor_w/(2*FL)) # rad
FoV_H = 2* wd*1000* np.tan(AoV_H/2) # mm
FoV_W = 2* wd*1000* np.tan(AoV_W/2) # mm
# FoV_H2 = sensor_h*wd*1000/FL # mm
# FoV_W2 = sensor_w*wd*1000/FL # mm

# Read image. 
img = cv2.imread('IMG1.bmp') 
  
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
print(detected_circles.shape)
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
        cv2.imshow("Detected Circle", img) 
        cv2.waitKey(0) 