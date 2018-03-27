# Class File does something with the file.

import csv
from collections import OrderedDict
from AminoAcid import AminoAcid

class CsvFile:
    def __init__(self):
        pass

    def open_csv_file(self, path):
        """
        :param path: path + filename
        :return: csv reader
        """
        file = open(path, newline='')
        reader = csv.reader(file)
        return reader

    def skip_header(self, reader):
        """
        :param reader: csv reader
        :return: header of the csv file
        """
        header = next(reader)
        return header

    def get_csv_values(self, reader, csv_file):
        """
        :param reader: cvs reader
        :return: data_dictionary: key = row_name  , value = [hydrofobicity, polarity, class_given]
        """
        data_dictionary = OrderedDict()
        data_list = []
        row_nr = 0
        for row in reader: # row = [polarity, hydrofobicity, given_class]
            row_nr, row_name = csv_file.name_rows(row_nr)
            polarity, hydrofobicity, given_class = int(row[0]), int(row[1]), int(row[2])
            data_dictionary[row_name] = [polarity, hydrofobicity, given_class]
            data = AminoAcid(polarity, hydrofobicity, given_class)
            data_list.append(data)
        return data_dictionary


    def name_rows(self, row_nr):
        """
        :param row_nr: row number of the previous row in the csv file.
        :return row_nr: row number of the current row.
        :return row_name: row name of the current row.
        """
        row_nr += 1
        row_name = "row_" + str(row_nr)
        return row_nr, row_name

