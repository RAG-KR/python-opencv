import os
import pickle

import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

"""importing all the states active marked etc etc
IMPORTING ALL THE MODE IMAGES INTO A LIST
 importing using list and getting full file link"""
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath , path)))
# print(len(imgModeList)) test that weve imported all the imgs correctly


"""load the encoded values"""
print("loading encoded file ...")
file = open('encodeFile.p' , 'rb')
encodeListWithIds = pickle.load(file)
file.close()
encodeListKnown , studentIds = encodeListWithIds
# print(studentIds)
print(" encoded file loaded !!!")


while True:
    success , img = cap.read()
    """the things inside the array are starting and ending points of the background 
    that we are using the ui basicaly"""
    imgBackground[162 :162+480 , 55:55+640] = img
    imgBackground[44 :44+633 , 808:808+414] = imgModeList[2]
    # cv2.imshow("webcam",img)

    cv2.imshow("face attandance",imgBackground)
    cv2.waitKey(1)
