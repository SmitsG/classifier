# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from CsvFile import CsvFile
import matplotlib.pyplot as plt

def main():
    csv_file = CsvFile()
    path = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_dictionary = csv_file.get_csv_values(reader, csv_file)
    class_predicted_dictionary = calculate_predictions(data_dictionary)
    error_dictionary = calculate_error(data_dictionary, class_predicted_dictionary)
    lowest_error_dictionary = calculate_lowest_error(error_dictionary)
    make_plot(lowest_error_dictionary)


def calculate_predictions(data_dictionary):
    """
    Calculate class predicted for each row in dataset, x times.
    :param data_dictionary: key - row_name  , value - [hydrofobicity, polarity, class_given]
    :return class_predicted_dictionary: key - row_name, value - predicted values for each row
    """
    class_predicted_dictionary = {}
    for i in range(50):
        times = "times_" + str(i)
        a, b = randomiser(0, 10) # Get a and b random values for Monte Carlo prediction.
        for row, data in data_dictionary.items(): # Do this x times the range
            class_predicted_value = calculate_class_predicted(data[0], data[1], a, b)
            class_predicted_dictionary.setdefault(times, []).append(class_predicted_value) #adds multiple values without overwriting
    return class_predicted_dictionary


def randomiser(lowest_value, highest_value):
    a = randint(lowest_value, highest_value)
    b = randint(lowest_value, highest_value)
    return a, b


def calculate_class_predicted(hydrofobicity, polarity, a, b):
    class_predicted_value = (a * hydrofobicity + b) - polarity
    return class_predicted_value


def calculate_error(data_dictionary, class_predicted_dictionary):
    error_dictionary = {}
    count = 0
    for times, predicted_class_list in class_predicted_dictionary.items():
        for predicted_class in predicted_class_list: # voor 70
            count += 1
            list_with_given_class = data_dictionary.get("row_" + str(count))
            error = ((list_with_given_class[2] - predicted_class) ** 2)
            error_dictionary.setdefault(times, []).append(error)
        count = 0

    return error_dictionary


def calculate_lowest_error(error_dictionary):
    lowest_error_dictionary = {}
    for times, error_list in error_dictionary.items():
        lowest_error_dictionary[times] = min(error_list)
    return lowest_error_dictionary


def make_plot(lowest_error_dictionary):
    x = 10
    y = 20
    plt.plot(x, y)



main()













#main
# predictions_dictionary = Caluculations.calculate_predictions(data_list)

#calculate
 # for data_object in data_list:
            # class_predicted = calculate.calculate_class_predicted(AminoAcid.get_hydrofobicity(data_object),
            #                                                       AminoAcid.get_polarity(data_object), a, b)
#
            # data_list = []
            # data = AminoAcid(polarity, hydrofobicity, given_class)
            # data_list.append(data)

  # get class predicted for each object in the data_list.
  #   and do this several amount of times (range).
  #   store the values for each time in a dictionary.