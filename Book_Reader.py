import cv2 # pip install opencv-python
import pytesseract #open the url:- https://medium.com/@marioruizgonzalez.mx/how-install-tesseract-orc-and-pytesseract-on-windows-68f011ad8b9b#:~:text=How%20install%20Tesseract%20%E2%80%94%20ORC%20and%20Pytesseract%20on,in%20your%20path%3F%20...%204%20Functionality%20test.%20?msclkid=b450aef2a9bc11eca0586aca2ea2f8fa
import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import time
def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()
def book_read():
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)

    while True:
        success, img = cap.read()
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow("Result1", img1)
            print(img1)
            print(pytesseract.image_to_string(img1)+"hello")
            speak(pytesseract.image_to_string(img1))
book_read()

