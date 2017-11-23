#!/usr/bin/python
# click on keepassX indicaton via shortcut. insert in shortcut list

import pyautogui

keepassLocation = pyautogui.locateCenterOnScreen('/opt/keepassx-shortcut/keepassx.png')
pyautogui.click(keepassLocation)

