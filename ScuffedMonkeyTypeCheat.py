import keyboard
import pyautogui
import time
import os
import pytesseract
from PIL import Image

# n is the number of repeat - 1
n = 10

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

keyboard.wait('F8')

pyautogui.screenshot(region=(185, 455, 1500, 180), imageFilename='file.png')

image = Image.open("file.png")

text = pytesseract.image_to_string(image)
text = text.replace('\n', ' ')

pyautogui.click()
pyautogui.write(text, interval=0.02)

# sectioning
while n > 0:
    pyautogui.screenshot(region=(185, 522, 1500, 100), imageFilename='file.png')

    image = Image.open("file.png")

    text = pytesseract.image_to_string(image)
    text = text.replace('\n', ' ')  

    pyautogui.click()
    pyautogui.write(text,interval=0.02)
    n-=1