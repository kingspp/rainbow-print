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

from abc import ABCMeta

class Singleton(type, metaclass=ABCMeta):
    """
    Singleton Class for
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]