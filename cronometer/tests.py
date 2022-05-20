from datetime import datetime
from os import system


def get_interval(string: str, milliseconds: int, clear: bool) -> None:
    if clear:
        system('cls')

    print('- Clock = {}' .format(datetime.now().strftime('%H:%M:%S:%f'))[:-2])
    print('- Cron. = {}.{:04}' .format(string, milliseconds))
    print()