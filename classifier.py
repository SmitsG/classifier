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
    data_list = csv_file.get_csv_values(path, reader)
    # a, b = randomiser(0, 9)
    # print(AminoAcid.get_hydrofobicity(data_list[1]))


# Class File does something with the file.
class CsvFile:

    def open_csv_file(self, path):
        file = open(path, newline='')
        reader = csv.reader(file)
        return(reader)

    def skip_header(self, reader):
        header = next(reader)

    def get_csv_values(self, path, reader):
        """
        :param path: filepath + filename
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
            data.get_hydrofobicity()
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
    
    def get_class_predicted(self, polarity, hydrofobicity):
        polarity = a * hydrofobicity + b

        return self.pred
    
    def calculate_error(self):
        return self.error


# def randomiser(lowest_value, highest_value):
#     a = randint(lowest_value, highest_value)
#     b = randint(lowest_value, highest_value)
#     return a, b


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