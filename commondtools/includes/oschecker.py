import platform


class OSChecker:

    @staticmethod
    def windows_only():
        if OSChecker.check_os() != "Windows":
            raise NotImplementedError("Windows only feature")

    @staticmethod
    def linux_only():
        if OSChecker.check_os() != "Linux":
            raise NotImplementedError("Linux only feature")

    @staticmethod
    def check_os() -> str:
        """
        e.g.: Linux, Windows
        :return:
        :rtype: str
        """
        return platform.system()
