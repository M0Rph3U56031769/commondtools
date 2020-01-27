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

    def getData(filename:str):
        import os

        dirname = os.path.dirname(__file__)
        dirname = os.path.dirname(dirname)
        return os.path.join(dirname, "data/"+filename)
    import os
    dirname = os.path.dirname(__file__)
    dirname = os.path.dirname(dirname)
    filename = os.path.join(dirname, getData(filename="example.csv"))
    csv_example = Reader(file=filename)
    csv_example.read()
