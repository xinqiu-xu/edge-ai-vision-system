import cv2

photo = cv2.imread("data/test.jpg")
if photo is None:
    print("无法读取图片")
    raise SystemExit

rgb_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", photo)
cv2.imshow("RGB Image", rgb_photo)
cv2.imshow("Grayscale Image", gray_photo)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("data/test_rgb.jpg", rgb_photo)
cv2.imwrite("data/test_gray_2.jpg", gray_photo)
