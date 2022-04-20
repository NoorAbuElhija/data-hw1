import math


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
    n=len(values)
    sum=0
    for i in range(n):
        sum=sum+((values[i]-avg)**2)
    sum=(1/n-1)*sum
    stdv=math.sqrt(sum)

    return stdv
def calc_covariance(values1, values2)

    avg1=calc_mean(values1)
    avg1=calc_mean(values2)
    sum=0
    n=len(values2)
    for i in range n:
        sum=sum+((values1[i]-avg1)*(values2[i]-avg2))
    cov=1/(n-1)*sum
    return cov
def population_statistics(feature_description, data, treatment, target, threshold, is_above,
statistic_functions)