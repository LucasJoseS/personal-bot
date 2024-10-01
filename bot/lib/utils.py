import pyautogui
import time


def press_sleep(s, sleep=0.1):
    pyautogui.press(s, 3, sleep)


def write_sleep(s, sleep=0.1):
    pyautogui.write(s, sleep)
    time.sleep(sleep)


def click_sleep(x, y, sleep=0.5):
    pyautogui.click(x, y)
    time.sleep(sleep)


def click_sleep_write(x, y, s, force=False):
    click_sleep(x, y, 0.2)

    if force:
        pyautogui.hotkey("ctrl", "a")

    write_sleep(s, 0.1)

    pyautogui.press('enter')
