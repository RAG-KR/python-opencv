import os

import cv2
import face_recognition
import pickle

# importing the student images
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath , path)))
    studentIds.append(os.path.splitext(path)[0])
    # print(path)
    # print(os.path.splitext(path)[0])
    """above line selected the first split of the 1057595.png=>"id"""
print(studentIds)

"""methd to encode the images and convert it into importable encodings"""
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("encoding started ... ")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown , studentIds]
print(encodeListKnown)
print("encoding complete !!!")


"""now we need to save these encodings so that we can imprt it when usign cam"""

file = open("encodeFile.p " , 'wb')
pickle.dump(encodeListKnownWithIds , file)
file.close()
print("endcoding file saved")