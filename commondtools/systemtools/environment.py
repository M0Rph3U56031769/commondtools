"""
General used methods for e.g. prevent screensaver

"""

import os
import platform
from ctypes import windll


class SystemTools:

    @staticmethod
    def win_only():
        if SystemTools.check_os() != "Windows":
            raise NotImplementedError("Windows only feature")

    @staticmethod
    def disable_lockscreen():
        """
        prevent screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        SystemTools.win_only()
        windll.kernel32.SetThreadExecutionState(0x80000002)

    @staticmethod
    def enable_lockscreen():
        """
        restore screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        SystemTools.win_only()
        windll.kernel32.SetThreadExecutionState(0x80000000)

    @staticmethod
    def get_username() -> str:
        return os.getlogin()

    @staticmethod
    def check_os() -> str:
        """
        e.g.: Linux, Windows
        :return:
        :rtype: str
        """
        return platform.system()
