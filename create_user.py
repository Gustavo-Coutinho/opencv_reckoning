from importlib.metadata import files
import os
import keyboard
import cv2


import time
# Load Camera
cap = cv2.VideoCapture(0)
role = str(input())
try:
    os.mkdir("images/" + role)
finally:
    name = str(input())
    filepath = "images/" + role + "/" + name + ".jpg"
    print("Press SPACE to capture or ESC to exit")
    while True:
        ret, frame = cv2.VideoCapture(0).read()
       # cv2.imshow("Frame", frame)

        if keyboard.read_key() == "space":

            print("Saving...")
            cv2.imwrite(filepath, frame)
            print("Saving...")
            break
     #   key = cv2.waitKey(1)
     #   if key == 27:
     #       # ESC pressed
     #       print("Escape hit, closing...")
     #       break
     #   elif key == 32:
     #       print("Saving...")
     #       cv2.imwrite(filepath, frame)
     #       break

    cap.release()
    cv2.destroyAllWindows()