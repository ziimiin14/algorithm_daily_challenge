import cv2
import numpy as np

image = cv2.imread('firstpic.png')
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)



if circles is not None:
	circles = np.round(circles[0, :]).astype("int")

    storeX = []
    storeY = []
    storeR = []
	for (x, y, r) in circles:
		cv2.circle(output, (x, y), r, (0, 0, 255), 0) ## Relative to first picture which is red color
        storeX.append(x)
        storeY.append(y)
        storeR.append(r)

    #check intersection
    # this part has not done yet no time to finished...
    if (abs(r[0]-r[1])<= np.sqrt((x[0]-x[1])**2+(y[0]-y[1])**2)<=(r[0]+r[1])):
        final_r = r[0] if r[0]>r[1] else r[1]
    else:
        fianl_r = storeR

	# show the output image
	cv2.imshow("output", np.hstack([image, output]))
	cv2.waitKey(0)

