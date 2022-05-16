import cv2

class FaceToID1():
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('C:/python-project/01_keras_yolo3_master/Face/trainer/trainer.yml')
        self.cascadePath = "C:\python-project\\01_keras_yolo3_master\Face\haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascadePath)

    def n_vs_n1(self, imageList):
        idList = []
        for img in imageList:
            cam = cv2.VideoCapture(0)
            # cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cam.set(3, 640)  # set video widht
            cam.set(4, 480)  # set video height
            # Define min window size to be recognized as a face
            minW = 0.1 * cam.get(3)
            minH = 0.1 * cam.get(4)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
                # Check if confidence is less them 100 ==> "0" is perfect match
                if (confidence < 100):
                    idList.append(id)
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = -1
                    idList.append(id)
                    confidence = "  {0}%".format(round(100 - confidence))
        cam.release()
        cv2.destroyAllWindows()
        return idList

if __name__ == '__main__':
    f = FaceToID1()
    img = cv2.imread("C:\\python-project\\HafetyHelmet\\idcard\\2.jpg")
    lista = []
    lista.append(img)
    print(f.n_vs_n1(lista))


