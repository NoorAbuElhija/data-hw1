import pandas as pd


def load_data(path, features):
    """load the data.

       Keyword arguments:
       path -- the path of the data file
       features -- specifications of the data
       """
    df = pd.read_csv(path)
    newdf = (df[features])
    data = newdf.to_dict(orient="list")
    # return data as dictionary
    return data


def filter_by_feature(data, feature, values):
    """divert the data .

          Keyword arguments:
          data -- dictionary that contains the data
          features -- specifications of the date to filter
          values -- set of values that the feature can get
          """
    data2 = {k: v.copy() for k, v in data.items()}
    data1 = {k: v.copy() for k, v in data.items()}
    i = 0
    j = 0
    k = 0
    while i < len(data[feature]):
        if data[feature][i] in values:
            for key in data:
                # delete the appropriate data from data2
                data2[key].pop(i - j)
            j = j + 1
        else:
            for key in data:
                # delete the inappropriate data from data1
                data1[key].pop(i - k)
            k = k + 1
        i = i + 1
    return data1, data2


def print_details(data, features, statistic_functions):
    """print statistical indices  .

             Keyword arguments:
             data -- dictionary that contains the data
             features -- specifications of the date to filter
             statistic_function -- list that contain statistic functions
             """
    for key in data:
        if key in features:
            print(key, end=": ")
            for i in range(len(statistic_functions)):
                avg = statistic_functions[i](data[key])
                formatf = "{:.2f}".format(avg)
                if i == 0:
                    print(formatf, end=", ")
                else:
                    print(formatf)


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    """print statistical indices  .

                 Keyword arguments:
                 data -- dictionary that contains the data
                 features -- specifications of the date to filter
                 statistic_function -- list that contain statistic functions
                 statistic_functions_names -- list that contains the name of statistic functions
                 """
    results = 0
    for i in range(len(statistic_functions)):
        results = statistic_functions[i](data[features[1]], data[features[0]])
    formatf = "{:.2f}".format(results)
    print(statistic_functions_names, formatf)
