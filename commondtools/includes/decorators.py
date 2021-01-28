from commondtools.includes.oschecker import OSChecker


def windows_only(func):
    def wrapper(*args, **kwargs):
        OSChecker.windows_only()
        func(*args, **kwargs)

    return wrapper


def linux_only(func):
    def wrapper(*args, **kwargs):
        OSChecker.linux_only()
        func(*args, **kwargs)

    return wrapper
