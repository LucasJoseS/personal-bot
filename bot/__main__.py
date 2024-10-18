from bot.lib.register import register
from sys import argv
from time import sleep
import re

regex = re.compile(r'(\w+) ref (\d+)00', re.IGNORECASE)

desc = argv[1]
value = regex.findall(desc)[0][1]

sleep(2)
register(
    desc,
    value_0=value,
    value_1=value,
    value_2=value,
    value_3=value,
    value_4=value
)
