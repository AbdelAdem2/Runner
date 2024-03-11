from djitellopy import Tello
import cv2
import keyboard

tello = Tello()
tello.connect()


if keyboard.on_press('O'):
    print('break')
    tello.streamon()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (960,720))

while True:
    frame = tello.get_frame_read().frame

    out.write(frame)

    cv2.imshow('Drone Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
out.release()
tello.streamoff()
tello.end()

