from bot.lib.utils import click, click_write, press


def _standart_sp():
    click(35, 255)
    click_write(490, 320, "49")
    click_write(490, 350, "49")
    click_write(260, 375, "1", True)


def _standart_ms():
    click(110, 255)
    click_write(490, 320, "49")
    click_write(490, 350, "49")
    click_write(260, 375, "104", True)


def _ncm(s: str):
    if not type(s) is str:
        raise TypeError(s)

    click_write(130, 180, s, True)
    press("enter", 4)
    press("esc")


def fiscal(s: str):
    if not type(s) is str:
        raise TypeError(s)

    click(150, 130)

    _ncm(s)
    _standart_sp()
    _standart_ms()
