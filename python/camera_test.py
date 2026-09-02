import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("无法打开摄像头")
    raise SystemExit

frame_count = 0
start_time = cv2.getTickCount()
fps = 0

while True:
    success, frame = camera.read()
    if not success:
        print("无法读取摄像头画面")
        break

    cv2.putText(frame, f"Resolution: {frame.shape[1]} x {frame.shape[0]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    frame_count += 1
    if frame_count == 30:
        end_time = cv2.getTickCount()
        fps = 30 / ((end_time - start_time) / cv2.getTickFrequency())
        frame_count = 0
        start_time = cv2.getTickCount()

    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Press q to quit", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()