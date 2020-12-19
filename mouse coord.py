import pyautogui
I = 1
while I == 1:
 currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
 print(currentMouseX, currentMouseY)
