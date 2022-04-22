import pandas as pd
from statistics import calc_mean
from statistics import calc_stdv
from statistics import calc_covariance
from statistics import population_statistics

def load_data(path, features):

    print(1)
    df = pd.read_csv(path)
    newdf = (df[features])
    data = newdf.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):

    data2 = {k:v.copy() for k,v in data.items()}
    data1 = {k:v.copy() for k,v in data.items()}
    i = 0
    j = 0
    l = 0
    while i < len(data[feature]):
        if data[feature][i] in values:
            for key in data:
                data2[key].pop(i-j)
            j=j+1
        else:
            for key in data:
                data1[key].pop(i-l)
            l=l+1
        i = i+1
    return data1, data2

def print_details(data, features, statistic_functions):
    j=0
    for key in data:
        if(key in features):
            print(key,end=":")
            for i in range(len(statistic_functions)):
                avg=statistic_functions[i](data[key])
                while avg < 10**j:
                    j = j + 1
                formatf= round(avg,2)
                if (i==0):
                    print(formatf,end=", ")
                else:
                    print(formatf)


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for i in range(len(statistic_functions)):
         cov = statistic_functions[i](data[features[1]],data[features[0]])
    format_float = round(cov,2)
    print(statistic_functions_names, format_float)
