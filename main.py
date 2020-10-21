#!/usr/bin/env python

import cv2
# img =cv2.imread('lena.jpg',1)
# print(img)
# cv2.imshow('image',img,)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
# cv2.imwrite('lena2.png',img)

# cap = cv2.VideoCapture(0);
# fourcc =cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
#
# while(True):
#     ret, frame = cap.read()
#
#     if ret == True:
#         print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#         out.write(frame)
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('video', gray)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
