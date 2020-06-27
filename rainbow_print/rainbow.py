# -*- coding: utf-8 -*-
"""
| **@created on:** 6/27/20,
| **@author:** prathyushsp,
| **@version:** v0.0.1
|
| **Description:**
| 
|
| **Sphinx Documentation Status:** 
"""

from sty import fg
import typing
import logging
from abc import ABCMeta
from rainbow_print.singleton import Singleton

class RainbowPrint(metaclass=Singleton):
    _DARK_VIOLET = fg(5, 152, 154)
    _DARK_INDIGO = fg(179, 128, 168)
    _DARK_BLUE = fg(112, 154, 180)
    _DARK_GREEN = fg(116, 162, 103)
    _DARK_YELLOW = fg(255, 255, 0)
    _DARK_ORANGE = fg(255, 127, 0)
    _DARK_RED = fg(255, 0, 0)

    _DARK_PALETTE = [_DARK_VIOLET, _DARK_GREEN, _DARK_INDIGO, _DARK_ORANGE, _DARK_BLUE, _DARK_YELLOW, _DARK_RED]

    _LIGHT_VIOLET = fg(54, 54, 54)
    _LIGHT_INDIGO = fg(139, 123, 139)
    _LIGHT_BLUE = fg(111, 153, 180)
    _LIGHT_GREEN = fg(85, 107, 46)
    _LIGHT_YELLOW = fg(128, 165, 32)
    _LIGHT_ORANGE = fg(255, 127, 0)
    _LIGHT_RED = fg(173, 71, 71)

    _LIGHT_PALETTE = [_LIGHT_VIOLET, _LIGHT_BLUE, _LIGHT_GREEN, _LIGHT_INDIGO, _LIGHT_ORANGE, _LIGHT_YELLOW, _LIGHT_RED]

    def __init__(self, theme: str = "dark", colors: typing.List[fg] = None):
        if colors is None:
            self.theme = theme
            if self.theme == 'dark':
                self.rainbow_colors = self._DARK_PALETTE
            elif self.theme == 'light':
                self.rainbow_colors = self._LIGHT_PALETTE
            else:
                raise Exception(f"Supported themes - {{light, dark}}. Given {self.theme}")
        else:
            self.theme = theme
            self.rainbow_colors = colors
        super().__init__()

    def _build_str(self, data: typing.Union[str, dict], sep):
        if isinstance(data, str):
            str_builder = ''
            for e, item in enumerate(data.split(sep)):
                str_builder += self.rainbow_colors[int(e % 7)] + f"{item}" + fg.rs + f'{sep}'
        elif isinstance(data, dict):
            str_builder = ''
            for e, (k, v) in enumerate(data.items()):
                str_builder += self.rainbow_colors[int(e % 7)] + f"{k}: {str(v)}" + fg.rs + f'{sep}'
        else:
            raise Exception(f'Supported types of data: [str, dict]. Given:{type(data)}')
        return str_builder[:-1]

    def __call__(self, data: typing.Union[str, dict], sep: str = ' | '):
        str_builder = self._build_str(data=data, sep=sep)
        print(str_builder)

    def update_palette(self, colors: typing.List[fg]):
        self.__init__(theme='custom', colors=colors)

    def update_dark_palette(self, colors: typing.List[fg]):
        self.__init__(theme='dark', colors=colors)

    def update_light_palette(self, colors: typing.List[fg]):
        self.__init__(theme='light', colors=colors)

    def set_dark_palette(self):
        self.__init__(theme='dark')

    def set_light_palette(self):
        self.__init__(theme='light')

    def info(self):
        print(f"Theme: {self.theme}\n"
              f"Colors: {self.rainbow_colors}")


printr = RainbowPrint()


class RainbowLogger():
    def __init__(self):
        self.logger = None

    def getLogger(self, name):
        self.logger = logging.getLogger(name=name)
        return self

    def info(self, message, sep=' | '):
        str_builder = printr._build_str(data=message, sep=sep)
        self.logger.info(str_builder)

    def debug(self, message, sep=' | '):
        str_builder = printr._build_str(data=message, sep=sep)
        self.logger.debug(str_builder)

    def error(self, message, sep=' | '):
        str_builder = printr._build_str(data=message, sep=sep)
        self.logger.error(str_builder)

    def warn(self, message, sep=' | '):
        str_builder = printr._build_str(data=message, sep=sep)
        self.logger.warn(str_builder)


rlogging = RainbowLogger()

if __name__ == '__main__':
    print("Dictionary Usage:")
    data_d = {"Episode": 10, "Episode Len": 5, "Cost": 0.95, "Reward": 135, "Mode": "Explore"}
    print("Default: \n", data_d)
    print("Printr: ")
    printr(data_d)
    print("\nString Usage:")
    data_s = f"Episode: {10}, Episode Len: {5}, Cost: {0.95}, Reward: {135}, Mode: {'Explore'}"
    print("Default: \n", data_s)
    print("Printr: ")
    print(data_s)
    printr(data_s, sep=',')
    print("\nInformation of configuration:")
    printr.info()