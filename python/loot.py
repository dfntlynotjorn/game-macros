from pywinauto.application import Application
import keyboard

window_title = str(input("Enter window title: "))

app = Application().connect(title = window_title)
window = app.window(title = window_title)

while True:
	window.type_keys("{VK_SPACE}")
	if keyboard.is_pressed('F6'):
		break