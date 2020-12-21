"""General calculus operations"""

import numpy as np


class Calculator:
    """General calculus operations"""

    @staticmethod
    def get_average(numbers: list):
        """
        returns the average of the numbers in the list

        :param numbers: list of numbers
        :type numbers: list
        :return: float
        """

        return np.average(numbers)
