import pyautogui
import time


def press(s, times=1, sleep=0.2):
    pyautogui.press(s, times, sleep)
    time.sleep(0.2)


def write(s, sleep=0.1):
    pyautogui.write(s, sleep)
    time.sleep(sleep)


def write_confirm(s, sleep=0.1):
    write(s, sleep)
    press("enter", sleep=sleep)


def click(x, y, sleep=0.5):
    pyautogui.click(x, y)
    time.sleep(sleep)


def click_write(x, y, s, force=False):
    if s is None:
        return

    click(x, y, 0.2)

    if force:
        pyautogui.hotkey("ctrl", "a")

    write(s, 0.1)

    pyautogui.press('enter')
