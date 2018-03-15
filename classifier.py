# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from CsvFile import CsvFile
import math
from AminoAcid import AminoAcid
# import matplotlib.pyplot as plt


def main():
    csv_file = CsvFile()
    path = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_dictionary, x_list, y_list = csv_file.get_csv_values(reader, csv_file)

    error_list = []
    minimum_error = 10000000000000

    for i in range(1000):
        a, b, c = randomiser(-10, 10) # Get a and b random values for Monte Carlo prediction.
        for row, data in data_dictionary.items(): # Do this x times the range
            class_predicted_value = calculate_class_predicted(data[0], data[1], a, b, c)
            error = calculate_error(data[2], class_predicted_value)
            error_list.append(error)
        sum_error = get_sum_error(error_list)

        if minimum_error > sum_error:
            minimum_error = sum_error
            a_opt = a
            b_opt = b
            c_opt = c
        else:
            minimum_error = minimum_error
        error_list = []

    print("min_error " + str(minimum_error))
    print("a_opt " + str(a_opt) + "\n" "b_opt " + str(b_opt) + "\n" "c_opt " + str(c_opt))

def randomiser(lowest_value, highest_value):
    a = randint(lowest_value, highest_value)
    b = randint(lowest_value, highest_value)
    c = randint(lowest_value, highest_value)
    return a, b, c


def calculate_class_predicted(x, y, a, b, c):
    # class_predicted_value = (-1 * x + 1 * y + 0)
    class_predicted_value = (a * x + b * y + c)
    return class_predicted_value


def calculate_error(given, class_predicted_value):
    error = (given - class_predicted_value) ** 2
    return error


def get_sum_error(error_list):
    sum_error = math.sqrt(sum(error_list))
    return sum_error


main()
