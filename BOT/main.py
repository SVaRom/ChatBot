import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)


position1=pt.locateOnScreen("BOT/smiley_paperclip_dark.png",confidence=.6)
x=position1[0]
y=position1[1]

#Gets messages
def get_message():
    global x,y
    position=pt.locateOnScreen("BOT/smiley_paperclip_dark.png",confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y,duration=.5)
    pt.moveTo(x+125,y-40,duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message=pyperclip.paste()
    pt.click()
    print("Message received: "+whatsapp_message)
    return whatsapp_message

#Posts
def post_response(message):
    global x,y
    position=pt.locateOnScreen("BOT/smiley_paperclip_dark.png",confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x+200,y+20,duration=.5)
    pt.click()
    pt.typewrite(message,interval=.01)
    pt.typewrite("\n", interval=.01)

# Processes response 
def process_response(message):
    random_no=random.randrange(3)
    if "hola" in str(message).lower():
        return "Hola jsjsjs"
    else: 
        if random_no==0:
            return "Je"
        elif random_no==1:
            return "Ma"
        else:
            return "xd"

#Check for new messages
def check_for_new_messages():
    pt.moveTo(x+110,y-40,duration=.5)
    while True:
        #Continiously checks for new green dots and new messages 
        try:
            position=pt.locateOnScreen("BOT/green_circle_dark.png",confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)

                pt.click()
                sleep(.5)
        except(Exception):
            print("No new other users with new messages located")
        if pt.pixelMatchesColor(int(x+110),int(y-40),(41,52,56),tolerance=10):#Positiosn,rgb color,tolerance DarkMode:RGB:41,52,56 LightMode:RGB:255,255,255
            #Note i don't recommend you to write more than 10 of tolerance !IMPORTANT
            print("is dark")
            processed_message=process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(5)


check_for_new_messages()

