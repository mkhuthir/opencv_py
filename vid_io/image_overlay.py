#!/usr/bin/python3

import cv2

# Load the overlay image. size should be smaller than video frame size
img = cv2.imread('../img/logo.png')

# Get Image dimensions
img_height, img_width, _ = img.shape

# Start Video Capture; 0 means capture from camera.
cap = cv2.VideoCapture(0)

# Get frame dimensions
frame_width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )

# Print dimensions
print('image dimensions (HxW):',img_height,"x",img_width)
print('frame dimensions (HxW):',int(frame_height),"x",int(frame_width))

# Decide X,Y location of overlay image inside video frame. 
# following should be valid:
#   * image dimensions must be smaller than frame dimensions
#   * x+img_width <= frame_width
#   * y+img_height <= frame_height
# otherwise you can resize image as part of your code if required

# Image location in the video frame
x = 20
y = 20

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Add image to frame
    frame[ y:y+img_height , x:x+img_width ] = img

    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()