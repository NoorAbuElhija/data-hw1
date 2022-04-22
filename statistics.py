
from math import sqrt

def calc_mean(values):

    i = 0
    sums=0
    for i in values:
        sums=sums+i
    n=len(values)
    avg=sums/ n
    return avg

def calc_stdv(values):
    avg=calc_mean(values)
    n=0
    n = len(values)
    sum=0
    for i in range(n):
        sum=sum+(values[i]-avg)*(values[i]-avg)

    stdv = sqrt((1/(n-1))*sum)
    return stdv
def calc_covariance(values1, values2):

    avg1=calc_mean(values1)
    avg2=calc_mean(values2)
    sum=0
    n=len(values2)
    for i in range (n):
        sum=sum+((values1[i]-avg1)*(values2[i]-avg2))
    cov=1/(n-1)*sum
    return cov

def population_statistics(feature_description, data, treatment, target, threshold, is_above,
statistic_functions):
    i = 0
    if (is_above):
        while i < len(data[treatment]):
            if data[treatment][i] < threshold:
                for key in data:
                    data[key].pop(i)
        i=+1
    else:
        while i < len(data[treatment]):
            if data[treatment][i] > threshold:
                for key in data:
                    data[key].pop(i)
        i=+1
    for j in range(len( statistic_functions)):
        result=statistic_functions[j](data[target])
        while result< 10 **k:
            k = k + 1
        formatf = round(result, 2)
        if (i == 0):
            print(formatf, end=", ")
        else:
            print(formatf)


