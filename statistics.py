
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
    k = 0
    i = 0
    data1=[]
    print(feature_description)
    print(target, end=": ")
    if is_above :
        while i < len(data[treatment]):
            if data[treatment][i] > threshold:
                data1.append(data[target][i])
            i = i+1
    else:
        while i < len(data[treatment]):
            if data[treatment][i] <= threshold:
                data1.append(data[target][i])
            i = i+1
    for j in range(len(statistic_functions)):
        result=statistic_functions[j](data1)
        formatf = round(result, 2)
        if (k==0):
            print(formatf, end=", ")
            k=k+1
        else:
            print(formatf)