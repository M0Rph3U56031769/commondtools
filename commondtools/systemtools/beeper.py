import time
import winsound
from typing import Iterable

from commondtools.includes.decorators import windows_only


class Beep:

    def __init__(self):
        pass

    @staticmethod
    @windows_only
    def beep(frequency: int, duration: int):
        """

        :param frequency: frequency of the beep
        :type frequency: int
        :param duration: duration in millisecond
        :type duration: int
        :return:
        """

        winsound.Beep(frequency=frequency, duration=duration)

    @staticmethod
    def morse_executor(code: Iterable[int],
                       frequency: int = 600,
                       short_duration: int = 400,
                       long_duration: int = 800,
                       delay: float = 0.1):
        """
        morse code generator
        1: long beep
        0: short beep

        :param delay:
        :param long_duration:
        :param short_duration:
        :param frequency:
        :param code:
        :return: None
        """

        if not isinstance(code, Iterable):
            raise TypeError("Use int type iterable!")
        for letter in code:
            if letter == 1:
                print("1 chosen")
                Beep.beep(frequency=frequency, duration=long_duration)
            elif letter == 0:
                print("0 chosen")
                Beep.beep(frequency=frequency, duration=short_duration)
                time.sleep(delay)
            else:
                print("Error at: {}".format(letter))
                raise TypeError("Use numbers 0 or 1")

    @staticmethod
    def split(word: str) -> list:
        """

        :param word: string to split. e.g.: '110011100'
        :type word: str
        :return: list of integers
        :rtype: list
        """

        string_list = [char for char in word]
        for i in range(len(string_list)):
            if type(string_list[i]) != int:
                raise TypeError
            string_list[i] = int(string_list[i])
        return string_list

    @staticmethod
    @windows_only
    def morse(code: Iterable[int], verbose: bool = False):

        if verbose:
            print("morse str: {}, {}".format(type(code), str(code)))

        Beep.morse_executor(code=code)


if __name__ == "__main__":
    print("Starting")
    Beep.morse_executor((1, 0, 1, 1, 0, 0, 1))
    Beep.morse_executor([0, 0, 0, 1, 1, 1, 0, 0, 0])
    Beep.morse_executor("asdasd")
    print("Finished")
