from bot.lib.utils import click_sleep_write, press_sleep
from bot.lib.fiscal import fiscal


def register(desc, barcode, price, group, ncm, save=False):
    # press_sleep("F2")

    click_sleep_write(145, 205, desc, True)
    click_sleep_write(105, 230, "un")
    click_sleep_write(115, 260, group, True)
    click_sleep_write(25, 630, "1", True)

    fiscal(ncm)

    if save:
        press_sleep("F10")
