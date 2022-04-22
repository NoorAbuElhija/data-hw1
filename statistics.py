
from math import sqrt

def calc_mean(values):

    i = 0
    sums=0
    while i < len(values):
        sums=sums+values[i]
        i=i+1
    avg=sums/i
    return avg

def calc_stdv(values):
    avg=calc_mean(values)
    n=0
    n = len(values)
    sum=0
    for i in range(n):
        sum=sum+((values[i]-avg)*(values[i]-avg))

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

    if(calc_mean() in statistic_functions) :
       mean = calc_mean(data[target])
       print(mean)
    if(calc_stdv() in statistic_functions):
       stdv = calc_stdv(data[target])
       print(stdv)
    if(calc_covariance() in statistic_functions):
       cov = calc_covariance(data[target])
       print(cov)