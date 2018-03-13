# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
from CsvFile import CsvFile
from AminoAcid import AminoAcid
# import matplotlib.pyplot as plt


def main():
    csv_file = CsvFile()
    path = "C:/Users/Beheerder/Documents/GitHub/classifier/input.csv"
    reader = csv_file.open_csv_file(path)
    header = csv_file.skip_header(reader)
    data_dictionary, x_list, y_list = csv_file.get_csv_values(reader, csv_file)

    # Non Monte Carlo
    # linear regression values
    b1, b0 = calculation(x_list, y_list)
    calc_error(b1, b0, x_list, y_list)

    # Monte Carlo
    time_error_dictionary = {}
    times_list = [10, 1000, 100000]
    for time in times_list:
        class_predicted_dictionary = calculate_predictions(data_dictionary, time)
        error_dictionary = calculate_error(data_dictionary, class_predicted_dictionary)
        lowest_error_dictionary = calculate_lowest_error(error_dictionary)
        print(time, lowest_error_dictionary)
    # make_plot(lowest_error_dictionary)


def calculate_predictions(data_dictionary, time):
    """
    Calculate class predicted for each row in dataset, x times.
    :param data_dictionary: key = row_name  , value = [hydrofobicity, polarity, class_given]
    :return class_predicted_dictionary: key = row (Monte Carlo), value = predicted for each time
    """

    class_predicted_dictionary = {}
    for i in range(time):
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
    :param data_dictionary: key = row_name  , value = [hydrofobicity, polarity, class_given]
    :param class_predicted_dictionary: key = row (Monte Carlo), value = predicted values for each row in the csv file.
    :return error_dictionary: key - times (Monte Carlo), value calculated error rate for each row of the csv file.
    """
    error_dictionary = {}
    for row, predicted_class_list in class_predicted_dictionary.items():
        for predicted_class in predicted_class_list:
            # error = given - predicted
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
        for error in error_list:
            lowest_error_dictionary[row] = error
    return lowest_error_dictionary


def make_plot(lowest_error_dictionary):
    pass
    # print(lowest_error_dictionary)
    # x = 10
    # y = 20
    # plt.plot(x, y)


################### Lineair regression formula ############################
def calculation(x_list, y_list):
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


def calc_error(b1, b0, x_list, y_list):
    predicted_value_list = []
    for x_value in x_list:
        estimate_value = b0 + b1 * x_value
        predicted_value_list.append(round(estimate_value, 2))

    y_minus_predicted_list_square = []
    for y_value, predicted_value in zip(y_list, predicted_value_list):
        y_minus_predicted = y_value - predicted_value
        y_minus_predicted_list_square.append(round(y_minus_predicted ** 2, 2))

    standard_error = (sum(y_minus_predicted_list_square) / (len(x_list) - 2))


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

############################################################################



main()

# je kan ook over de gehele reeks 10000 x Monte Carlo doen, in plaats van voor elke row X times een suspected te berekenen.
# miss toch 100, 200, 300 iteratie maken. En dan
# randomizer aanpassen?