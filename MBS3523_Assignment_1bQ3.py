import cv2
import numpy as np

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
width = cam.get(3)
height = cam.get(4)
print(height,width)

while True:
    ret, frame = cam.read()

    flipped_horizontally = cv2.flip(frame, 1)  # Flip horizontally
    flipped_vertically = cv2.flip(frame, 0)  # Flip vertically
    flipped_both = cv2.flip(frame, -1)  # Flip both horizontally and vertically

    top_row = np.hstack((frame, flipped_horizontally))
    bottom_row = np.hstack((flipped_vertically, flipped_both))
    combined_image = np.vstack((top_row, bottom_row))

    cv2.imshow('cam', combined_image)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()