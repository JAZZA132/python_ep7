import pyautogui as pag
import  os
import  time
import win32gui
import win32con
import win32api
from PIL import Image
import math
import operator
# from functools import reduce
# from fuzzywuzzy import fuzz
import pyautogui

# hwnd_title = dict()
# def _get_all_hwnd(hwnd, mouse):
#  if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#   hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

# try:
#     while True:
#         print("Press Ctrl-C to end")
#         screenWidth, screenHeight = pag.size()  #獲取螢幕的尺寸
#         print(screenWidth,screenHeight)
#         x,y = pag.position()   #獲取當前滑鼠的位置
#         posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
#         print(posStr)
#         time.sleep(0.2)
#         os.system('cls')   #清楚螢幕
# except KeyboardInterrupt:
#     print('end....')

hwndMain = win32gui.FindWindow(None, "夜神模擬器")
# win32gui.MoveWindow(hwndMain,900,100,1000,500,False)
left,top,right,bottom = win32gui.GetWindowRect(hwndMain)
# print(left,top,right,bottom)
win32gui.SetForegroundWindow(hwndMain) #畫面至頂



# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
i= pyautogui.locateOnScreen('equipment.png')
print(i)
pag.moveTo(1383,206,duration=0.5) #拖曳滑鼠
pag.dragTo(1383,top-20,button='left')
