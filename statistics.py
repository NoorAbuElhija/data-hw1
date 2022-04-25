from math import sqrt


def calc_mean(values):
    """calculate the average.

        Keyword arguments:
        values -- list of numbers to calculate there average
        """
    sums = 0
    for i in values:
        sums = sums + i
    n = len(values)
    avg = sums / n
    # return the average
    return avg


def calc_stdv(values):
    """calculate the std.

        Keyword arguments:
        values -- list of numbers to calculate there std
        """
    sums = 0
    avg = calc_mean(values)
    n = len(values)
    for i in range(n):
        sums = sums + (values[i] - avg) * (values[i] - avg)

    stdv = sqrt((1 / (n - 1)) * sums)
    # return the std
    return stdv


def calc_covariance(values1, values2):
    """calculate the covariance.

        Keyword arguments:
        values1 -- the first list of samples
        values2 -- the second list of samples to calculate the covariance
        """
    sum1 = 0
    avg1 = calc_mean(values1)
    avg2 = calc_mean(values2)
    n = len(values2)
    for i in range(n):
        sum1 = sum1 + ((values1[i] - avg1) * (values2[i] - avg2))
    cov = 1 / (n - 1) * sum1
    # return the covariance
    return cov


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):
    """ calculate and print statistical indices  .

                    Keyword arguments:
                    feature_description -- string that describe a group
                    data -- dictionary that contains the data
                    treatment -- name of a feature from database
                    target -- name of a feature from database
                    threshold -- threshold value for treatment
                    is_above -- indicator that can be True or False
                    statistic_functions -- list that contain statistic functions
                    """
    k = 0
    i = 0
    data1 = []
    print(feature_description)
    print(target, end=": ")
    if is_above:
        while i < len(data[treatment]):
            if data[treatment][i] > threshold:
                # add the appropriate target value to data
                data1.append(data[target][i])
            i = i + 1
    else:
        while i < len(data[treatment]):
            if data[treatment][i] <= threshold:
                data1.append(data[target][i])
            i = i + 1
    for j in range(len(statistic_functions)):
        # calculate the statistical indices
        result = statistic_functions[j](data1)
        if k == 0:
            # print the mean
            formatf = "{:.2f}".format(result)
            print(formatf, end=", ")
            k = k + 1
        else:
            # print the std
            formatf = "{:.2f}".format(result)
            print(formatf)
