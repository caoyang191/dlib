import numpy as np
import cv2

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


img = cv2.imread(r'1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chess board corners
corners = cv2.goodFeaturesToTrack(gray,200,0.01,10)

# If found, add object points, image points
objpoints.append(objp)

# 亚像素角点检测
corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
imgpoints.append(corners2)

# Draw and display the corners
img = cv2.drawChessboardCorners(img, (7,6), corners2,False)
cv2.imshow('img',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
