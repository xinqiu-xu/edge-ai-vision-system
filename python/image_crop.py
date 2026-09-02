import cv2

photo = cv2.imread('data/test.jpg')
if photo is None:
    print("无法读取图片")
    raise SystemExit

height = photo.shape[0]
width = photo.shape[1]

y1 = int(height /3)
y2 = int(2 * height /3)
x1 = int(width /3)
x2 = int(2 * width /3)

cropped_photo = photo[y1:y2, x1:x2]

cv2.imshow("Original Image", photo)
cv2.imshow("Cropped Image", cropped_photo)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("data/test_crop.jpg", cropped_photo)