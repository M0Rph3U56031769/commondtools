import os
import unittest
from pathlib import Path
from unittest import TestCase

from .csvmanager import CSVManager


class TestCSVManager(TestCase):
    i = CSVManager(str(Path(os.getcwd()).parent))

    def test_check_csv_integrity_false(self):
        self.assertFalse(self.i.check_csv_for_empty_cells(
            [['a', 'b', 'c'],
             ['1', '', '3'],
             ['', '2', '3'],
             ['1', '', ''],
             ['1', '2', '3']]))

    def test_check_csv_integrity_true(self):
        self.assertTrue(self.i.check_csv_for_empty_cells([['a', 'b', 'c'],
                                                          ['1', '2', '3']]))

    def test_check_csv_for_diff_types_true(self):
        self.assertTrue(self.i.check_csv_for_diff_types([['a', 'b', 'c'],
                                                         ['x', 0, 'i'],
                                                         ['y', 1, 'j']]))

    def test_check_csv_for_diff_types_false(self):
        self.assertFalse(self.i.check_csv_for_diff_types([['a', 'b'],
                                                          ['x', 0],
                                                          ['y', 'i']]))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
