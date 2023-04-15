import win32gui
import win32api
import pyautogui
import pydirectinput
import subprocess
import time
from config import Config
from download_and_extract_mgba import download_and_extract_mgba


def setup_mgba():
	download_and_extract_mgba(Config.mgba_link())

	print(f"Opening {Config.mgba_executable_file_path()}...")
	if len(Config.rom_file_value()) != 0:
		subprocess.Popen(
			[
				Config.mgba_executable_file_path(),
				f"-{int(Config.mgba_scaling_value())}",
				Config.rom_file_value(),
			]
		)
	else:
		subprocess.Popen(
			[Config.mgba_executable_file_path(), f"-{int(Config.mgba_scaling_value())}"]
		)

	time.sleep(5)
	print("Ready!")

	# Returns the handle of the window titled UNTITLED
	handle = win32gui.FindWindow(None, "mGBA")
	print(f"Using handle {handle}")
	return handle


def press(button: str, hld: int):
	key = ""
	if len(button) <= len("select"):
		if button == "a":
			key = "x"
		elif button == "b":
			key = "z"
		elif button == "left":
			key = button
		elif button == "right":
			key = button
		elif button == "up":
			key = button
		elif button == "down":
			key = button
		elif button == "select":
			key = "backspace"
		elif button == "start":
			key = "enter"
		else:
			return
	else:
		return

	if hld > 0:
		try:
			win32gui.SetForegroundWindow(hld)
		except Exception:
			pass
		pydirectinput.press(key)
