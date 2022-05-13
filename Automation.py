from pyautogui import *
import pyautogui
import time
import os
import colorama
from colorama import Fore

colorama.init(autoreset=False)

onGoingTime = 0


# move to follow button on the home page
def moveToFollowButton():
    xFollow = 681
    yFollow = 849
    pyautogui.moveTo(xFollow, yFollow)
    pyautogui.click()


# move to instagram follow button
def profileFollowButton():
    # Following user
    # check if Follow image is on the screen
    if pyautogui.locateOnScreen('Capture.png', confidence=0.9) != None:
        print(Fore.YELLOW + "following user + 2 Credits")
        # get x and y value of the follow button stored in the list
        values = pyautogui.locateOnScreen('Capture.png', confidence=0.9)
        # move mouse to follow button with x and y cords
        pyautogui.moveTo(values[0] + 5, values[1] + 5)
        # click follow button
        pyautogui.click()

        # find like button in the screen
    elif pyautogui.locateOnScreen('shareV2.png', confidence=0.6) != None:
        print(Fore.LIGHTCYAN_EX + "liking post + 1 Credits")
        # stored in to values, is a list
        values = pyautogui.locateOnScreen('shareV2.png', confidence=0.5)
        # get x and y of the like button and move to there
        pyautogui.moveTo(values[0] + 2, values[1] + 2)
        # click on the like button
        pyautogui.click()
    else:
        # if the page did not load it will say error
        print(Fore.RED + "WEB PAGE ERROR")


# check if already followed the user
def ifFollowed():
    if pyautogui.locateOnScreen('followed.png', confidence=0.8) != None:
        print("Already Followed")
        return True
    return False


# exit the pop up window
def exitWindow():
    windowX = 1895
    windowY = 12
    pyautogui.moveTo(windowX, windowY)
    pyautogui.click()


# verify
def verify():
    verifyX = 831
    verifY = 862
    pyautogui.moveTo(verifyX, verifY)
    pyautogui.click()


# full screen the pop up window
def fullSizeScreen():
    fullScreenX = 938
    fullScreenY = 14
    pyautogui.moveTo(fullScreenX, fullScreenY)
    pyautogui.click()


# refresh window
def refreshWindow():
    reX = 79
    reY = 39
    pyautogui.moveTo(reX, reY)
    pyautogui.click()


while (True):
    time.sleep(2)
    moveToFollowButton()
    time.sleep(3)
    fullSizeScreen()
    time.sleep(3)
    if (ifFollowed() == True):
        exitWindow()
        continue
    else:
        profileFollowButton()
        time.sleep(3)
        exitWindow()
        time.sleep(3)
        verify()
        time.sleep(5)
    # if like or follow 5 times refresh the window
    if (onGoingTime == 5):
        refreshWindow()
        onGoingTime = 0
        print(Fore.WHITE + "Refreshed")
        time.sleep(5)

    onGoingTime += 1


