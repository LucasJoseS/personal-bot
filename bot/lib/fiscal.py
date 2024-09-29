import pyautogui
import time


def click_sleep(x, y, sleep=0.5):
    pyautogui.click(x, y)
    time.sleep(sleep)


def click_sleep_write(x, y, s):
    pyautogui.click(x, y)
    time.sleep(0.2)

    pyautogui.write(s, 0.1)
    time.sleep(0.2)

    pyautogui.press('enter')


def standart_sp():
    click_sleep(35, 255)
    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "1")


def standart_ms():
    click_sleep(110, 255)
    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "104")


def fiscal():
    click_sleep(150, 130)

    standart_sp()
    standart_ms()
