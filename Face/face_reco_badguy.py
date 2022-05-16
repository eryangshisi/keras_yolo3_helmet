import cv2
from PIL import Image
import numpy

class FaceToID():
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('C:/python-project/01_keras_yolo3_master/Face/trainer/trainer.yml')

    def n_vs_n(self, imageList):
        idList = []
        for img in imageList:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # gray = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_BGR2GRAY)
            id, confidence = self.recognizer.predict(gray)
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                # 认识他
                confidence = "  {0}%".format(round(100 - confidence))
                idList.append(id)
            else:
                id= -1
                idList.append(id)
                confidence = "  {0}%".format(round(100 - confidence))
        return idList


if __name__ == '__main__':
    f = FaceToID()
    img = cv2.imread("C:\\python-project\\HafetyHelmet\\idcard\\20200303007.jpg")
    lista = []
    lista.append(img)
    print(f.n_vs_n(lista))