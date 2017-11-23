#!/usr/bin/python

# click on keepassX indicaton via shortcut. insert in shortcut list

import pyautogui

keepassLocation = pyautogui.locateCenterOnScreen('keepassx.png')
pyautogui.click(keepassLocation)

