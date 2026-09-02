import cv2

photo = cv2.imread("data/test.jpg")
if photo is None:
    print("无法读取图片")
    raise SystemExit

height = photo.shape[0]
width = photo.shape[1]

small_photo = cv2.resize(photo, (width // 2, height // 2))
gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", photo)
cv2.imshow("Small Image", small_photo)
cv2.imshow("Gray Image", gray_photo)

if cv2.waitKey(0) & 0xFF == ord('q'):   
    cv2.destroyAllWindows()

cv2.imwrite("data/test_small.jpg", small_photo)
cv2.imwrite("data/test_gray.jpg", gray_photo)