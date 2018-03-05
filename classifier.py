# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from CsvFile import CsvFile
# import matplotlib.pyplot as plt


def main():
    csv_file = CsvFile()
    path = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_dictionary, data_list, x_list, y_list, given_list = csv_file.get_csv_values(reader, csv_file)
    b1, b0 = calculation(x_list, y_list)

def calculation(x_list, y_list):
    print(x_list, y_list)
    x_mean = mean(x_list)
    y_mean = mean(y_list)

    # x - x̄
    # y - ȳ
    x_diff_list, y_diff_list = [], []
    for polarity, hydrofobicity in zip(x_list, y_list):
        x_diff_list.append(round(polarity - x_mean, 2))
        y_diff_list.append(round(hydrofobicity - y_mean, 2))

    # (x - x̄)2
    x_diff_square_list = []
    for x_diff in x_diff_list:
        square_diff = x_diff ** 2
        x_diff_square_list.append(round(square_diff,2))

    # sum_x_diff_square_list (x - x̄)2
    sum_x_diff_square_list = sum(x_diff_square_list)

    # (x - x̄) * (y - ȳ)
    x_minus_y_list = []
    for x_diff, y_diff in zip(x_diff_list, y_diff_list):
        x_minus_y_list.append(round(x_diff * y_diff, 2))

    # sum (x - x̄) * (y - ȳ)
    sum_x_minus_y_list = sum(x_minus_y_list)

    # calculate b1
    b1 = sum_x_minus_y_list / sum_x_diff_square_list

    # Ŷ = b0 + b1 * x , calculate b0
    b0 = abs(y_mean - b1 * x_mean)

    return b1, b0

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)





main()