import cv2
import pytesseract
import speech_recognition as sr # pip install speechRecognition
import pyttsx3 # pip install pyttsx3
import time
def speak(str):
    engine.say(str)
    engine.runAndWait()
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
engine = pyttsx3.init()
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("Result1", img1)
        print(img1)
        print(pytesseract.image_to_string(img1)+"hello")
        speak(pytesseract.image_to_string(img1))


