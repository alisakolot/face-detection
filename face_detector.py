import cv2

# Load some pre-trianed data on face frontals from opencv (haar cascade algorithm)
# cv2: call library
# Cascade
# Classifier:  detector, classifies something as face
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose image to detect faces in 
    # this is how you import img into open cv
    # imread: image read 
    # img is a 2d array of numbers
img = cv2.imread('rdj.jpg')

# Convert to Grascale 
    # easy to deal w one number/binary instead of three/rgb
    # cvtColor: convert color, params: source img, 
    # **BGR = RBG, cv2 quirk 
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

# Detect Faces
    # trained_face_Data: face classifier
    # detectMultiScale: detects objects of different sizes in input image, 
        # can detect face regardless of size
    #  gives us coordinates of rectangle surrounding the face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)
# results in [top left coordinate, width, height, bottom right point]

# Draw Rectangles Around Faces 
    # coordinates: (x+w, y+h)
        #  take x and add width
        # take y and add height to it
    # (0, 255, 0): color of square, B [G] R
    # 2 :  thickness of rectangle
# cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
cv2.rectangle(img, (260,  95), (260+217, 95+217), (0, 255, 0), 2)




# imshow: image show
# 'Clever Programmer Face Detector': name of window that pops up
# img [refer to var above] the image you want to display
cv2.imshow('Clever Programmer Face Detector', img)

# waitkey: needed or otherwise image closes instantly by pausing execution of your code
    # waiting until a key is pressed, closes on keystroke
cv2.waitKey() 




print("Code complete")

