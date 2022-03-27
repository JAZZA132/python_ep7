import  os
import  time
import win32gui
import win32con
import win32api
from PIL import Image
import math
import operator
import pyautogui as pag

# python基於win32實現窗口截圖
# hwnd_title = dict()
# def _get_all_hwnd(hwnd, mouse):
#  if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#   hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
# win32gui.EnumWindows(_get_all_hwnd, 0)
# for wnd in hwnd_title.items():
#  print(wnd)

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
if win32gui.IsIzconic(hwndMain):
    win32gui.ShowWindow(hwndMain,win32con.SW_SHOWMAXIMIZED)
win32gui.SetForegroundWindow(hwndMain) #畫面至頂
print(hwndMain)
time.sleep(0.5)




img= pag.locateOnScreen('2w9.png',confidence=0.9) #判斷螢幕上的圖片做別
time.sleep(1)
if img == None:
    print("沒有")
    pag.moveTo(left+500,bottom-100,duration=1) #拖曳滑鼠
    time.sleep(0.3)
    pag.dragTo(left+500,bottom-300,duration=1) #拖曳滑鼠
    time.sleep(0.3)
    img2= pag.locateOnScreen('2w9.png',confidence=0.9)
    time.sleep(0.3)
    if img2 == None:
        #沒找到 刷新
        print('也沒有')
        pag.press('z',interval=0.25)
        time.sleep(0.3)
        pag.press('space',interval=0.25)
        time.sleep(0.3)
    else:
        #下拉後找到
        print(img2)

else:
   print(img)
