import cv2
from random import randrange
import playsound_check


# Load some pre-trianed data on face frontals from opencv (haar cascade algorithm)
# cv2: call library
# Cascade
# Classifier:  detector, classifies something as face
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose image to detect faces in 
    # this is how you import img into open cv
    # imread: image read 
    # img is a 2d array of numbers
# img = cv2.imread('ba_rdj.jpg')

"""Webcam Source:"""
# can add filename instead of 0
webcam = cv2.VideoCapture(0)
# key = cv2.waitKey(1)

# play file 
playsound_check.Play()

previous_coord_lst = []
# Iterate forever over frames:
while True:
    
    # Read the current frame
    # returns tuples: 1. if reading the frame was successful, 2. frame/actual img
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    """Detect Faces"""
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    print(face_coordinates)
    if len(face_coordinates) == 0:
        continue

    # if any([[529, 8, 400, 400], [670, 328, 228, 228]]):
    #     playsound_check.ExitPlayer()
    # else:
    #     playsound_check.Play()
    
    """Get list of coordinates, to get data on initial position"""
    # resetting default coording and face coord lst
    
    face_coord_lst = []
    # face_coord_lst: box for one frame
    face_coord_lst.append(face_coordinates)

    # keep largest rectangle in face_coordinates
    # function that takes arg x and multiplies it by third/fourth element together
    face_coordinates = [max(face_coordinates, key = lambda x: x[2] * x[3])]

    """Framing/Frame Color"""
    for (x, y, w, h) in face_coordinates:
        # pulling frame from line 27 when webcam unpacks
        cv2.rectangle(frame, (x,y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5)
        # check if diagonal in current rect is the same as diagonal in previous rect
        

        # compute how big the movement is


        # og face_coord_lst is previous face coord
        # current face_coord has to be recorded after several seconds 
    
    # resetting the previous coords
    # estimated moving window
    # need to keep an avg
    previous_coord_lst = face_coordinates


    # find the center of the frame
    
        
        
    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1) #number is
    
    # Stop if Q is pressed
        # numbers represent ascii code
    if key == 81 or key == 113:
        break
    # print(face_coord_lst)
    


 

# Convert to Grayscale 
    # easy to deal w one number/binary instead of three/rgb
    # cvtColor: convert color, params: source img, 
    # **BGR = RBG, cv2 quirk 
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

# Detect Faces
    # trained_face_Data: face classifier
    # detectMultiScale: detects objects of different sizes in input image, 
        # can detect face regardless of size
    #  gives us coordinates of rectangle surrounding the face
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)
# results in [top left coordinate, width, height, bottom right point]

# Draw Rectangles Around Faces 
    # coordinates: (x+w, y+h)
        #  take x and add width
        # take y and add height to it
    # (0, 255, 0): color of square, B [G] R
    # 2 :  thickness of rectangle
# cv2.rectangle(img, (260,  95), (260+217, 95+217), (0, 0, 255), 5) <=hard coding coordinates
# (below) automatically assigns var in face_coordinates to tuple, 0 bc list within list 
    #  multiple faces results in face_coordinates turning into list of lists
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5)




# Display Image With Faces
    # imshow: image show
    # 'Clever Programmer Face Detector': name of window that pops up
    # img [refer to var above] the image you want to display
# cv2.imshow('Clever Programmer Face Detector', img)

# waitkey: needed or otherwise image closes instantly by pausing execution of your code
    # waiting until a key is pressed, closes on keystroke
# cv2.waitKey() 



print('*****', face_coordinates)
print("Code complete")

