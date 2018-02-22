# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import csv

def main():
    csv_file = File()
    path = "C:/Users/gerwi/PycharmProjects/classifier/input.csv"
    data_list = csv_file.get_csv_values(path)


# Class File does something with the file.
class File:

    def get_csv_values(self, path):
        """
        :param path: filepath + filename
        :return: data_list: List with data objects [obj1: polarity, hydrofobicity, given class, obj2 ...]
        """
        file = open(path, newline='')
        reader = csv.reader(file)
        data_list = []

        header = next(reader)
        data = []
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
    
    def get_class_predicted(self):
        return self.pred
    
    def get_error(self):
        return self.error
        

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