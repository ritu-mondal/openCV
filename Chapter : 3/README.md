```python
import cv2

org_img = cv2.imread("/Users/sahi/Skills/OpenCV/#Phase-2/image.png")

flip_img_0 = cv2.flip(org_img, 0)
flip_img_1 = cv2.flip(org_img, 1)
flip_img_neg1 = cv2.flip(org_img, -1)

cv2.imshow("Flip code : 0", flip_img_0)
cv2.imshow("Flip code : 1", flip_img_1)
cv2.imshow("Flip code : -1", flip_img_neg1)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
