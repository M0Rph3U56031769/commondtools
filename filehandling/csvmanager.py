"""
Managing csv files with data type(float, str) validator
"""

import csv
import logging
import sys
from os import listdir
from os.path import isfile, join

import pandas as pd


class CSVManager:
    """
    CSVManager is able to handle easily csv files with validation.
    """

    csv_path: str
    csv_files: list
    logger = logging.getLogger('Importer')
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __init__(self, current_path: str):
        self.csv_path = current_path
        self.logger.setLevel(logging.DEBUG)
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def get_all_data_as_list(self):
        """
        Getting all the csv data as a list.
        :return: all the csv content in a list.
        """
        return self.read_all_csv()

    def get_csv_files(self):  # pragma: no cover
        """
        Get the list of csv file names

        :return: list of csv file names
        """

        module_path = self.csv_path
        csv_files = [f for f in listdir(module_path) if isfile(join(module_path, f))
                     and ".csv" in f]
        self.csv_files = list(csv_files)
        return csv_files

    def check_csv_for_diff_types(self, csv_reader: list):
        """
        Checking for different types in rows

        NOTE: only checking str and float types (no datetime and such)

        NOTE2: sale/incoming can be used as a boolean type

        :param csv_reader: csv file content
        :type csv_reader: list
        :return: Bool
        """

        self.logger.debug(csv_reader)
        # read content by rows without header
        dataframe = pd.DataFrame(csv_reader)
        columns = []
        for column_name in dataframe.columns.array:
            columns.append(dataframe[column_name].to_numpy())
        for column in columns:
            data_type = ''
            for cell in column:
                try:
                    float(cell)
                    data_type = 'float'
                except ValueError:
                    if data_type == 'float':
                        logging.error('cannot convert to a float: ' + str(cell))
                        return False
        return True

    def check_csv_for_empty_cells(self, csv_reader: list):
        """
        Checking for empty cells
        :param csv_reader: csv file content
        :type csv_reader: list
        :return: Bool: integrity
        """

        self.logger.debug(csv_reader)
        integrity = True
        for row in csv_reader:
            for cell in row:
                if cell in (None, ""):
                    logging.error("Empty cell found at: " + str(row))
                    integrity = False
        return integrity

    def read_all_csv(self):
        """
        reading all csv files
        :return: list: all the csv contents in a list
        """

        content = []
        try:
            self.get_csv_files()
        except AttributeError:
            self.get_csv_files()
        self.logger.debug(self.csv_files)
        for file in self.csv_files:
            print(file)
            content.append(self.read_csv_file(file=file))
        return content

    def read_csv_file(self, file: str):
        """
        read the content of a single csv file
        :param file: csv file name
        :type file: str
        :return: list: csv content
        """

        content = []
        with open(self.csv_path + "/" + file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            self.check_csv_for_empty_cells(csv_reader=list(csv_reader))
            self.check_csv_for_diff_types(csv_reader=list(csv_reader))

        with open(self.csv_path + "/" + file, 'r') as csv_file:
            for row in csv.reader(csv_file):
                content.append(row)
        return content
