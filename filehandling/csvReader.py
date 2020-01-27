import csv


class Reader:
    file: str = None
    delimiter: str = ','

    def __init__(self, file: str, delimiter: str = ','):
        self.file = file
        self.delimiter = delimiter

    def read(self):
        csv_header: list = []
        csv_table: dict = {}

        with open(file=self.file, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    csv_header.append(row)
                else:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
            print(f'Processed {line_count} lines.')


if __name__ == "__main__":

    def getData(file_name:str):
        import os

        directory_name = os.path.dirname(__file__)
        directory_name = os.path.dirname(directory_name)
        return os.path.join(directory_name, "data/" + file_name)
    csv_example = Reader(file=getData(file_name="example.csv"))
    csv_example.read()
