from bot.lib.utils import click_write
from bot.lib.fiscal import fiscal


def register(
    desc: str,

    group: str = None,
    un: str = "un",
    supplier: str = None,

    # Value for each store
    value_0: str = None,
    value_1: str = None,
    value_2: str = None,
    value_3: str = None,
    value_4: str = None,


    ncm: str = None,

    _create_edit: bool = True,
    _save: bool = True,
):
    click_write(145, 205, desc)
    click_write(105, 230, un)
    click_write(115, 260, group)

    click_write(305, 410, value_0, True)
    click_write(305, 425, value_1, True)
    click_write(305, 440, value_2, True)
    click_write(305, 460, value_3, True)
    click_write(305, 475, value_4, True)

    click_write(25, 640, supplier)

    fiscal(ncm)
