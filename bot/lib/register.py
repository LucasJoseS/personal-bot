from bot.lib.utils import click_write
from bot.lib.fiscal import fiscal


def register(
    desc: str,
    group: str,
    supplier: str = "1",
    un: str = "un",

    ncm: str = None
):
    click_write(145, 205, desc)
    click_write(105, 230, un)
    click_write(115, 260, group)
    click_write(25, 640, supplier)

    if ncm is not None:
        fiscal(ncm)
