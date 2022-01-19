# imports of needed libraries
import cv2, sys, numpy, os

###########################################################################################################################
# LOCAL VARIABLES TO CHANGE FOR NEEDS #####################################################################################
###########################################################################################################################
# specifies the dimensions of the camera
(width, height) = (130, 100)

# specifies the method how faces are recognized
face_classificator = 'haar_cascade_frontal.xml'
project_path = os.path.curdir
datasets = 'datasets'
sub_data = 'videodata'

###########################################################################################################################
# ################################### #####################################################################################
###########################################################################################################################

####################################################################################
def create_dataset_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("Dataset directory created.")
    else:
        print("Dataset directory already exists.")
####################################################################################

dataset_folder_path = os.path.join(project_path, datasets, sub_data)
create_dataset_directory(dataset_folder_path)

face_cascade = cv2.CascadeClassifier(face_classificator)
webcam = cv2.VideoCapture(0)

count = 1
while count < 30:
    (_, image) = webcam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # draw a rectangle around the recognized face
    for(xCell, yCell, faceWidth, faceHeight) in faces:
        cv2.rectangle(image, (xCell, yCell), (xCell + faceWidth, yCell + faceHeight), (255, 0, 0), 2)
        face = gray[yCell:yCell + faceHeight, xCell:xCell + faceWidth]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('% s/% s.png' % (dataset_folder_path, count), face_resize)
    count += 1

    cv2.imshow('OpenCV', image)
    key = cv2.waitKey(10)
    if key == 27:
        break

