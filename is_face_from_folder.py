import cv2
import face_recognition
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# LOAD MESSI-2
img2 = cv2.imread("images/messi-2.jpg")
#rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

face_locations, face_names = sfr.detect_known_faces(img2)
for face_loc, name in zip(face_locations, face_names):
    top, right, bottom, left = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    cv2.putText(img2, name,(left, top -15), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
    cv2.rectangle(img2, (left, top), (right, bottom), (0, 0, 200), 2)
    print(name)

cv2.imshow("Img 2", img2)
cv2.waitKey(0)