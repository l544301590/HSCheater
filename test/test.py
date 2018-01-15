import os
import win32gui
from const import *
import logging


def catch_hs_window():
    """Set hs window to foreground

    title_name is reference to by spy++
    :return:
    """
    _class = HSWIN_CLASS_NAME if HSWIN_CLASS_NAME else None
    _title = HSWIN_TITLE_NAME if HSWIN_TITLE_NAME else None
    catch_window(_class, _title)


def catch_window(class_name, title_name):
    handle = win32gui.FindWindow(class_name, title_name)
    if handle:
        win32gui.SetForegroundWindow(handle)
    logging.warning("HearthStone Window is not found!")
