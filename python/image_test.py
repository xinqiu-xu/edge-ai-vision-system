import cv2

photo = cv2.imread("data/test.jpg")
if photo is None:
    print("无法读取图片")
    raise SystemExit

cv2.imshow("Image Test", photo)

key = cv2.waitKey(0) & 0xFF
if key == ord('q'):
    cv2.destroyAllWindows()

cv2.imwrite("data/test_copy.jpg", photo)