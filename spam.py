# required libraries 
import time 
import pyautogui

#to set time to allow user to scan whatsapp qr
time.sleep(10)

#message
message="suren"
 
#number of times to send message
num_messages=200

#coordinates for input box on whatsapp web
input_box_x= 738
input_box_y= 955

#click on input box
pyautogui.click(x=input_box_x , y=input_box_y)

#sending multiple messages
for i in range(num_messages):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(0)
