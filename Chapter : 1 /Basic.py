# import lib

import cv2

cv2.__version__ # for check OpenCv Version

img = cv2.imread("785807834991593260.jpeg")  # Load img 

# img_name = openCV_library.imagea-read-function(___img path___)

# for display new_img

cv2.imshow("Window Title", img)

# openCV_library.image-show-function( title_name , img_name )
cv2.waitKey(5000)  # cv2. wait-function ( time-in-sec )  ## (0) --> special_number_ 
cv2.destroyAllWindows() # --> close-open_img window 
