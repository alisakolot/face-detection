"""Webcam Motion Detector"""
import cv2, time, pandas
# import datetime from datetime library (used for frame comparison later)
from datetime import datetime 
# import sound 
import playsound_check


# Assign static_back to None
static_back = None

# Lists when any moving object appears
motion_list = [None, None]

# Time of movement
time = []

# Initializing DataFrame, one column is start time and the other is
    # end time 
    # DataFrame: 2 dimensional labeled data structure, similar to SQL 
    # or dict of Series obj
df = pandas.DataFrame(columns = ["Start", "End"])

# Capturing Video
video = cv2.VideoCapture(0)

# Infinite loop to treat livestream of images as video
while True: 
    # Reading frame/images from video
    check, frame = video.read()

    # Initializing motion = 0 (no motion)
    motion = 0

    # Converting color image to gray_scale (for cv)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Converting gray scale image to GaussianBlur so change can be 
    # detected easily 
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # In the first iteration of the while loop the static_back var is 
        # assigned to our first frame 
    if static_back is None:
        static_back = gray
        continue

    # Difference between static background and current frame (which is GaussianBlur)
    diff_frame = cv2.absdiff(static_back, gray)

    # If the change between static background/static_back and 
        # current grame is greater than 30 it will show up white
    thresh_frame = cv2.threshold(diff_frame, 30, 355, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
    # Finding the contour of the moving object
    cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts: 
        if cv2.contourArea(contour) <  10000:
            continue
        # else: 
        #     playsound_check.Play()
        motion = 1

        (x, y, w, h) = cv2.boundingRect(contour)

        # keep largest rectangle in face_coordinates
        # function that takes arg x and multiplies it by third/fourth element together
        # face_coordinates = [max(face_coordinates, key = lambda x: x[2] * x[3])]
        
        # making green rectangle arround the moving obj
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Appending the status of motion
    motion_list.append(motion)
    motion_list = motion_list[-2:]

    # Appending Start time of motion
    if motion_list[-1] ==  1 and motion_list[-2] == 0:
        time.append(datetime.now())

    # Appending end tiem of motion
    if motion_list[-1] == 0 and motion_list[-2] == 1:
        time.append(datetime.now())
    
    # Displaying image in gray_scale
    cv2.imshow("Gray Frame", gray)

    # Displaying the difference in current frame to the static frame(first frame)
    cv2.imshow("Difference Frame", diff_frame)

    # Displaying the bw imaage in which if the intensity diff is greater than 30
        # it will appear white
    cv2.imshow("Threshold Frame", thresh_frame)

    # Displaying color frame with contour of motion of object
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)


    # stopping the process with q
    if key == ord('q'):
        # if something is moving, the end time of the movement is appended
        if motion == 1:
            time.append(datetime.now())
        break

    # appending time of motion in DataFrame
    for i in range(0, len(time), 2):
        df = df.append({"Start": time[i], "End": time[i + 1]}, ignore_index = True)

        # Create a CSV file in which time of movement will be saved 
        df.to_csv("Time_of_movement.csv")

        video.release()

        # Destroy all the windows
        cv2.destroyAllWindows()