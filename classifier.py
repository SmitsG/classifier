# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from CsvFile import CsvFile
import math
import matplotlib.pyplot as plt
import random
from itertools import islice

def main():
    csv_file = CsvFile()
    path = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_dictionary = csv_file.get_csv_values(reader, csv_file)

    training_set_size = (2 / 3)
    number_training_instances = calculate_number_training_instances(data_dictionary, training_set_size)
    training_data, testing_data = split_train_test_instances(data_dictionary, number_training_instances)
    print("training_data" + training_data)
    print("test_data" + testing_data)

    minimum_error, a_opt, b_opt, c_opt, times = get_minimum_error_and_opt_values(data_dictionary)


# Function that gets 2/3 for the training set and 1/3 for the test set
def calculate_number_training_instances(data_dictionary, training_set_size):
    return int(round((len(data_dictionary) * training_set_size), 0))


def split_train_test_instances(dataset, number_training_instances):
    it = iter(dataset)
    for i in xrange(0, len(dataset), 1000):
        yield {k:dataset[k] for k in islice(it, 1000)}

    random.shuffle(dataset)
    training_data = []
    for item in range(number_training_instances):
        random.shuffle(dataset)
        index = random.randint(0, len(dataset) - 1)
        placeholder = dataset.pop(index)
        training_data.append(placeholder)
    testing_data = dataset
    return training_data, testing_data


# Trainings_set
# This function uses Monte Carlo to predict the optimal a, b and c values. And the minimum errors.
def get_minimum_error_and_opt_values(data_dictionary):
    """
    :param data_dictionary:
    :return:
    """
    error_list = []
    minimum_error = 10000000000000
    minimum_error_dict = {}

    times = 11
    for time in range(times):
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

        minimum_error_dict[time] = minimum_error
        error_list = []

    print(minimum_error_dict)
    plot(minimum_error_dict, times)

    return minimum_error, a_opt, b_opt, c_opt, times

# Test_set


# Generates random values
def randomiser(lowest_value, highest_value):
    a = randint(lowest_value, highest_value)
    b = randint(lowest_value, highest_value)
    c = randint(lowest_value, highest_value)
    return a, b, c


# Calculates the predicted values
def calculate_class_predicted(x, y, a, b, c):
    """
    :param x, y: x and y values received from the dataset
    :param a, b, c: random values
    :return: class_predicted_value
    """
    # class_predicted_value = (-1 * x + 1 * y + 0)
    class_predicted_value = (a * x + b * y + c)
    return class_predicted_value


# Calculates the error for each row of the dataset.
def calculate_error(given, class_predicted_value):
    """
    :param given: given class value
    :param class_predicted_value:  predicted class value
    :return: error for a certain row
    """
    error = (given - class_predicted_value) ** 2
    return error


# Calculates the sum of the errors in a dataset.
def get_sum_error(error_list):
    """
    :param error_list: list that contains the errors for each row in a dataset.
    :return: sum of all errors in the dataset.
    """
    sum_error = math.sqrt(sum(error_list))
    return sum_error


# Plots a chart with the minimum errors against the amount of times.
def plot(minimum_error_dict, times):
    """
    :param minimum_error_dict:
    :param times:
    :return:
    """

    minimum_error_list = []
    time_list = []
    for time, minimum_error in minimum_error_dict.items():
        time_list.append(time)
        minimum_error_list.append(minimum_error)
    plt.plot(minimum_error_list, time_list)

    plt.show()


main()
