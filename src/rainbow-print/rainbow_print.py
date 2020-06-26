# -*- coding: utf-8 -*-
"""
| **@created on:** 6/19/20,
| **@author:** prathyushsp,
| **@version:** v1.0.0
|
| **Description:**
|
|
| **Sphinx Documentation Status:**
"""

__all__ = ['printr', 'RainbowPrint']

from sty import fg
import typing


class RainbowPrint(object):
    DARK_VIOLET = fg(5, 152, 154)
    DARK_INDIGO = fg(179, 128, 168)
    DARK_BLUE = fg(112, 154, 180)
    DARK_GREEN = fg(116, 162, 103)
    DARK_YELLOW = fg(255, 255, 0)
    DARK_ORANGE = fg(255, 127, 0)
    DARK_RED = fg(255, 0, 0)

    DARK_PALETTE = [DARK_VIOLET, DARK_GREEN, DARK_INDIGO, DARK_ORANGE, DARK_BLUE, DARK_YELLOW, DARK_RED]

    LIGHT_VIOLET = fg(54, 54, 54)
    LIGHT_INDIGO = fg(139, 123, 139)
    LIGHT_BLUE = fg(111, 153, 180)
    LIGHT_GREEN = fg(85, 107, 46)
    LIGHT_YELLOW = fg(128, 165, 32)
    LIGHT_ORANGE = fg(255, 127, 0)
    LIGHT_RED = fg(173, 71, 71)

    LIGHT_PALETTE = [LIGHT_VIOLET, LIGHT_BLUE, LIGHT_GREEN, LIGHT_INDIGO, LIGHT_ORANGE, LIGHT_YELLOW, LIGHT_RED]

    def __init__(self, theme: str = "dark", colors: typing.List[fg] = None):

        if colors is None:
            self.theme = theme
            if self.theme == 'light':
                self.rainbow_colors = self.DARK_PALETTE
            elif self.theme == 'dark':
                self.rainbow_colors = self.LIGHT_PALETTE
            else:
                raise Exception(f"Supported themes - {{light, dark}}. Given {self.theme}")
        else:
            self.theme = theme
            self.rainbow_colors = colors

    def __call__(self, string: str = None, data_dict: dict = None, sep: str = '|'):
        if string is not None:
            pass
        elif data_dict is not None:
            str_builder = ''
            for e, (k, v) in enumerate(data_dict.items()):
                str_builder += self.rainbow_colors[int(e % 7)] + f"{k}: {str(v)}" + fg.rs + ' | '
            print(str_builder)
        else:
            raise Exception('Either provide string or data_dict. No data to print')

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

    def update_theme(self, theme: str):
        self.__init__(theme=theme)

    def info(self):
        print(f"Theme: {self.theme}\n"
              f"Colors: {self.rainbow_colors}")


printr = RainbowPrint()
