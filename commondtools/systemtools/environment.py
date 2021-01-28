"""
General used methods for e.g. prevent screensaver

"""

import os
from ctypes import windll

from commondtools.includes.decorators import windows_only


class SystemTools:

    @staticmethod
    @windows_only
    def disable_lockscreen():
        """
        prevent screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        windll.kernel32.SetThreadExecutionState(0x80000002)

    @staticmethod
    @windows_only
    def enable_lockscreen():
        """
        restore screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        windll.kernel32.SetThreadExecutionState(0x80000000)

    @staticmethod
    @windows_only
    def get_username() -> str:
        """
        get the current os user name
        :return:
        """
        return os.getlogin()


if __name__ == "__main__":
    SystemTools.disable_lockscreen()
    print(SystemTools.get_username())
    SystemTools.enable_lockscreen()
