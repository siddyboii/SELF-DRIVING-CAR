
""" import cv2
vidcap = cv2.VideoCapture('myvid2.mp4')
success,image = vidcap.read()
count = 0
while success:
  success,image = vidcap.read()
  resize = cv2.resize(image, (640, 480)) 
  cv2.imwrite("%03d.jpg" % count, resize)
  cv2.imshow("vid",image)     
  if cv2.waitKey(1) & 0xFF == ord("s"):                     
      break
  count +=1 """

import cv2
import os


img_path = "C:/Users/SIDH/Python/SelfDriving/vid1.mp4"

if os.path.exists(img_path):
    img = cv2.imread(img_path)
    if img is not None:
        img_resized = cv2.resize(img, (480, 280))
        # Do something with the resized image
        print("blahblah")
    else:
        print("Error: Failed to read image file")
else:
    print("Error: File does not exist")
