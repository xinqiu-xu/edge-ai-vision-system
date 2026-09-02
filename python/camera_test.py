import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("无法打开摄像头")
    raise SystemExit

while True:
    success, frame = camera.read()
    if not success:
        print("无法读取摄像头画面")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()