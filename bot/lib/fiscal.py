from bot.lib.utils import click_sleep, click_sleep_write, press_sleep


def standart_sp():
    click_sleep(35, 255)
    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "1", True)


def standart_ms():
    click_sleep(110, 255)
    click_sleep_write(490, 320, "49")
    click_sleep_write(490, 350, "49")
    click_sleep_write(260, 375, "104", True)


def ncm(s):
    click_sleep_write(130, 180, s, True)
    press_sleep("enter")


def fiscal(s):
    click_sleep(150, 130)

    ncm(s)
    standart_sp()
    standart_ms()
