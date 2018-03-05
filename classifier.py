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
    data_dictionary = csv_file.get_csv_values(reader, csv_file)
    times_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for times in times_list:
        class_predicted_dictionary = calculate_predictions(data_dictionary, times)
        error_dictionary = calculate_error(data_dictionary, class_predicted_dictionary)
        lowest_error_dictionary = calculate_lowest_error(error_dictionary)
        # give lowest errors to plot
    # make_plot(lowest_error_dictionary)


def calculate_predictions(data_dictionary, times):
    """
    Calculate class predicted for each row in dataset, x times.
    :param data_dictionary: key - row_name  , value - [hydrofobicity, polarity, class_given]
    :return class_predicted_dictionary: key - times (Monte Carlo), value - predicted values for each row in the csv file.
    """

    class_predicted_dictionary = {}
    for i in range(times):
        a, b = randomiser(0, 10) # Get a and b random values for Monte Carlo prediction.
        for row, data in data_dictionary.items(): # Do this x times the range
            class_predicted_value = calculate_class_predicted(data[0], data[1], a, b)
            class_predicted_dictionary.setdefault(row, []).append(class_predicted_value) # adds multiple values without overwriting
    return class_predicted_dictionary


def randomiser(lowest_value, highest_value):
    """
    :param lowest_value: lowest value for randomizing
    :param highest_value: highest value for randomizing
    :return: random value a, random value b
    """
    a = randint(lowest_value, highest_value)
    b = randint(lowest_value, highest_value)
    return a, b


def calculate_class_predicted(hydrofobicity, polarity, a, b):
    """
    :param hydrofobicity: Hydrofobicity of a certain row in the csv file.
    :param polarity: Polarity of a certain row in the csv file.
    :param a: random value a
    :param b: random value b
    :return: The class_predicted value.
    """
    class_predicted_value = (a * hydrofobicity + b) - polarity
    return class_predicted_value


def calculate_error(data_dictionary, class_predicted_dictionary):
    """
    :param data_dictionary: key - row_name  , value - [hydrofobicity, polarity, class_given]
    :param class_predicted_dictionary: key - times (Monte Carlo), value - predicted values for each row in the csv file.
    :return error_dictionary: key - times (Monte Carlo), value calculated error rate for each row of the csv file.
    """
    error_dictionary = {}
    for row, predicted_class_list in class_predicted_dictionary.items():
        for predicted_class in predicted_class_list:
            error = ((data_dictionary.get(row)[2] - predicted_class) ** 2)
            error_dictionary.setdefault(row, []).append(error)
    return error_dictionary


def calculate_lowest_error(error_dictionary):
    """
    :param error_dictionary: key - times (Monte Carlo), value calculated error rate for each row of the csv file.
    :return lowest_error_dictionary: key - times (Monte Carlo), value - lowest error calculated from all rows in the csv file.
    """
    lowest_error_dictionary = {}
    for row, error_list in error_dictionary.items():
        len(error_list)
        for error in error_list:
            pass
    return lowest_error_dictionary


def make_plot(lowest_error_dictionary):
    pass
    # print(lowest_error_dictionary)
    # x = 10
    # y = 20
    # plt.plot(x, y)


main()