import cv2
image_name="Poisson"
img = cv2.imread(f'{image_name}.PNG',1)
cv2.imshow("img",img)
img_shape= img.shape
print (img_shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = 255-gray
#cv2.imshow("dst",dst)
#cv2.waitKey()
cv2.imwrite(f'{image_name}_inverted.PNG', dst)