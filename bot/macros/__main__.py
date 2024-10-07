from pynput import keyboard
from bot.lib.fiscal import fiscal


def fiscal_command():
    fiscal("")


with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+f': fiscal_command,
}) as hotkeys:
    hotkeys.join()
