import win32gui
import win32api
import pyautogui
import pydirectinput
import subprocess
import time

def setup_mgba(mgba_executable):
	gba_file = input("Path to Pokemon ROM: ")
	subprocess.Popen([mgba_executable, gba_file])
	time.sleep(10)
	print("Ready!")
	hld = win32gui.FindWindow (None, "mGBA") # Returns the handle of the window titled UNTITLED

	return hld

def press(button, hld):
	key = ''
	if len(button) <= len('select'):
		if button == 'a': key = 'x'
		elif button == 'b': key = 'z'
		elif button == 'left': key = button
		elif button == 'right': key = button
		elif button == 'up': key = button
		elif button == 'down': key = button
		elif button == 'select': key = 'backspace'
		elif button == 'start': key = 'enter'
		else: return
	else: return
	
	if hld > 0:
			try:
				win32gui.SetForegroundWindow(hld)
			except Exception:
				pass
			pydirectinput.press(key)