# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
from random import randint


def main():
    csv_file = CsvFile()
    path = "C:/Users/gerwi/PycharmProjects/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_list = csv_file.get_csv_values(reader)
    a, b = randomiser(0, 9)
    # print(AminoAcid.get_hydrofobicity(data_list[2]))
    class_predicted_list = AminoAcid.get_class_predicted(data_list, a, b)


# Class File does something with the file.
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

    def get_csv_values(self, reader):
        """
        :param reader: cvs reader
        :return: data_list: List with data objects [obj1: polarity, hydrofobicity, given class, obj2 ...]
        """
        data_list = []

        for row in reader:
            # row = [polarity, hydrofobicity, given_class]
            polarity = int(row[0])
            hydrofobicity = int(row[1])
            given_class = int(row[2])
            data = AminoAcid(polarity, hydrofobicity, given_class)
            data_list.append(data)
        return data_list


# Class AminoAcid stores amino_acid values.
class AminoAcid:
    def __init__(self, polarity, hydrofobicity, given):
        self.pol = polarity
        self.hyd = hydrofobicity
        self.giv = given
        
    def get_polarity(self):
        return self.pol
    
    def get_hydrofobicity(self):
        return self.hyd
    
    def get_class_given(self):
        return self.giv
    
    def get_class_predicted(data_list, a, b):
        class_predicted_list = []
        for hyd, pol in data_list.get_hydrofobicity(), data_list.get_polarity():
            hydrofobicity = AminoAcid.get_hydrofobicity(data_list[hyd])
            polarity = AminoAcid.get_hydrofobicity(data_list[pol])
            class_predicted = (a * hydrofobicity + b) - polarity
            class_predicted_list.append(class_predicted)
        return class_predicted_list
    
    def calculate_error(self):
        pass


def randomiser(lowest_value, highest_value):
    a = randint(lowest_value, highest_value)
    b = randint(lowest_value, highest_value)
    return a, b


main()

# with open(path, "r") as csv_file:
#     reader = csv.reader(csv_file)
#     header = next(reader)
#     for row in reader:
#         print(row)
#         if re.match(r'^\d', row):
#             start = True
#         if start == True:
#              row = row.strip()
#              row = row.split(",")
#              obj = Amino_acid(row[0], row[1], row[2])
#              obj_valuelist.append(obj)
# return obj_valuelist