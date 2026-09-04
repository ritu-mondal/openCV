import cv2 

img = cv2.imread("/Users/sahi/Skills/OpenCV/#Phase-2/ok.jpg")

if img is not None:
  crop_imp = img[120:160,20:100] # crop_img_name = iamge[X1:X2 , Y1;Y2]
  ## diplay img function :
  cv2.imshow("old_img",img)
  cv2.imshow("crop_img",crop_imp)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

### Image Rotation

# M = cv2.getROtationMatrix2D(center,angle,scale)
    #  center --> pairs of number 
    # angle ---> 90, -90 ( clck wise)
    # scale ---> zoom in zoom out 
 
# rotation_img = cv2.warpAffine(orginal_img,M,(width,height))

org_img = cv2.imread("/Users/sahi/Skills/OpenCV/#Phase-2/ok.jpg")

if org_img is None:
  print("could not find any img")

else :
  (h,w) = org_img.shape[:2]
  center = (w//2 , h//2)
  M = cv2.getRotationMatrix2D(center , 90 ,1.0)
  rotated = cv2.warpAffine(org_img,M,(w,h))
  cv2.imshow("Orginal img : ",org_img)
  cv2.imshow("rotated_img : ", rotated)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


### Flip Image

# flipped = cv2.flip(img,flip_code)

# 0 -> flip vertically (top -> bottom)
# 1-> horizontally flip ( left-right)
# -1-> both ( H+ V)

org_img = cv2.imread("/Users/sahi/Skills/OpenCV/#Phase-2/image.png")

flip_img_0 = cv2.flip(org_img,0)
flip_img_1 = cv2.flip(org_img,1)
flip_imp_neg1 = cv2.flip(org_img,-1)

cv2.imshow("flip code : 0", flip_img_0)
cv2.imshow("flip code : 1" ,flip_img_1)
cv2.imshow("flip code : -1",flip_imp_neg1)
cv2.waitKey(0)
cv2.destroyAllWindows()
