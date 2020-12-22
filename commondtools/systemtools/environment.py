"""
General used methods for e.g. prevent screensaver

"""

from ctypes import windll


class SystemTools:

    @staticmethod
    def disable_lockscreen():
        """
        prevent screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        windll.kernel32.SetThreadExecutionState(0x80000002)

    @staticmethod
    def enable_lockscreen():
        """
        restore screensaver/lock screen

        source:
        https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

        """

        windll.kernel32.SetThreadExecutionState(0x80000000)


if __name__ == "__main__":
    SystemTools.disable_lockscreen()
    input("Press enter to exit...")
    SystemTools.enable_lockscreen()
