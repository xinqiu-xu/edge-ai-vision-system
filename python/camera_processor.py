import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("无法打开摄像头")
    raise SystemExit

mode = "color"
frame_count = 0
start_time = cv2.getTickCount()
fps = 0

while True:
    success, frame = camera.read()
    if not success:
        print("无法读取摄像头画面")
        break

    frame_count += 1
    if frame_count == 30:
        end_time = cv2.getTickCount()
        fps = 30 / ((end_time - start_time) / cv2.getTickFrequency())
        frame_count = 0
        start_time = cv2.getTickCount()
        
    if mode == "grayscale":
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == "color":
        frame = frame

    cv2.putText(frame, f"Resolution: {frame.shape[1]}x{frame.shape[0]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Camera Processor", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('g'):
        mode = "grayscale"
    elif key == ord('c'):
        mode = "color"
    elif key == ord('s'):
        cv2.imwrite("data/snapshot.jpg", frame)
        print("已保存当前帧为 snapshot.jpg")
    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()