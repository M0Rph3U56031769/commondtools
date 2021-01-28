import platform

from commondtools.includes.exceptions import NotImplementedYet


class OSChecker:

    @staticmethod
    def windows_only():
        if OSChecker.check_os() != "Windows":
            raise NotImplementedYet()
            # raise NotImplementedError("Windows only feature")

    @staticmethod
    def linux_only():
        if OSChecker.check_os() != "Linux":
            raise NotImplementedYet()
            # raise NotImplementedError("Linux only feature")

    @staticmethod
    def check_os() -> str:
        """
        e.g.: Linux, Windows
        :return:
        :rtype: str
        """
        return platform.system()


if __name__ == "__main__":
    OSChecker.linux_only()
