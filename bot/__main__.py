import pyautogui
import time


def click_sleep_write(x, y, s):
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.write(s)


def standart_sp():
    pyautogui.click(35, 255)
    time.sleep(0.2)

    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "1")


def standart_ms():
    pyautogui.click(110, 255)
    time.sleep(0.2)

    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "104")


def fiscal():
    standart_sp()
    standart_ms()


time.sleep(3)
fiscal()
