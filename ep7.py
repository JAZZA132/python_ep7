import win32gui
import win32con
import pyautogui 
import time
 

#pyautogui.displayMousePosition() #滑鼠座標偵測
def refresh(): #刷新商店
    pyautogui.press('z', interval=0.5)
    pyautogui.press('z', interval=0.1)
    time.sleep(0.4)
    pyautogui.press('space', interval=0.5)
    pyautogui.press('space', interval=0.1)
    time.sleep(0.4)

def buy(l,h): #購買物品
    pyautogui.moveTo(l+620, h+55, duration=0.2)
    time.sleep(0.4)
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.press('b', interval=0.25)
    pyautogui.press('b', interval=0.25)
    time.sleep(0.4)

def rolldown(): #往下拉
    pyautogui.moveTo(980, 560, duration=0.2)
    time.sleep(0.3)
    pyautogui.dragTo(980, 200, duration=1)  # 拖曳滑鼠
    time.sleep(0.6)
    



#目標物品
target = 'good1.png'
target2 = 'good2.png'

#執行次數
rounds=50

#目標視窗
hwnd = win32gui.FindWindow(None, 'BlueStacks 1')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
if win32gui.IsIconic(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
win32gui.SetForegroundWindow(hwnd)
time.sleep(0.2)


x = 0
bookmark=0
golden=0
try:
    while x < rounds:
        counted=0
        x = x+1
        refresh()
        book = pyautogui.locateOnScreen(target, confidence=0.9)
        gold = pyautogui.locateOnScreen(target2, confidence=0.9)
        time.sleep(0.2)
        if book != None or gold != None:
            if book != None:
                print(book)
                bookmark=bookmark+1
                l=book.left
                h=book.top
                buy(l,h)
                counted=1
            if gold != None:
                print(gold)
                golden=golden+1
                l=gold.left
                h=gold.top
                buy(l,h)
                counted=1

        rolldown()
        book2 = pyautogui.locateOnScreen(target, confidence=0.9)
        gold2 = pyautogui.locateOnScreen(target2, confidence=0.9)
        time.sleep(0.2)
        if book2 != None or gold2 != None:
            # 下拉後找到
            if book2 != None:
                print(book2)
                if counted==0:
                    bookmark=bookmark+1
                l=book2.left
                h=book2.top
                buy(l,h)
            if gold2 != None:
                print(gold2)
                if counted==0:
                    golden=golden+1
                l=gold2.left
                h=gold2.top
                buy(l,h)

        else:
            #沒找到
            print(x,'沒找到')
            if x >14 and golden==0 and bookmark==0 :
                print(x,'太雖了= =')
                break
            
    else:
        print('刷了',x,'次,得到神秘',golden,'次,書籤',bookmark,'次')

except KeyboardInterrupt:
    pass

'''

print(left,top,right,bottom)
im = ImageGrab.grab(
  bbox=(0,0,1920,1080))
im.save("box.png")
'''

'''
#OCR的部分
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")
img_name = './screenshot.jpg'
img = Image.open(img_name)


text = pytesseract.image_to_string(img, lang='chi_tra')


print(text)
'''


'''
import ctypes
import win32gui
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        print(buff.value)
        titles.append((hwnd, buff.value))
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)


找到所有視窗

'''
