import pytesseract
import os
import cv2
from PIL import Image

if not os.path.exists('images_frames'):
    os.makedirs('images_frames')

test_vid = cv2.VideoCapture('videoplayback.mp4')
index = 0
while test_vid.isOpened():
    for i in range(0,30):
        ret, frame = test_vid.read()
    if not ret :
        break
    name = './images_frames/frame' + str(index) + '.png'
    print('Extracting frames....' + name)
    cv2.imwrite(name, frame)
    index += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
test_vid.release()
cv2.destroyAllWindows()
n = index
while index:
    curr = "./images_frames/frame" + str(n-index) + ".png"
    index -= 1
    demo  = Image.open(curr)
    text = pytesseract.image_to_string(demo, lang = 'eng')
    print(text)
