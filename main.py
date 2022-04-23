# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import sys
import pandas as pd
from data import load_data
from data import filter_by_feature
from data import print_details
from data import print_joint_details
from statistics import calc_mean
from statistics import calc_stdv
from statistics import calc_covariance
from statistics import  population_statistics



def main(argv):

   features = ['hum', 't1', 'cnt', 'season', 'is_holiday']

   path = 'C:\\Users\\noor2\\OneDrive\\Desktop\\data\\london_sample.csv'

   data = load_data(path, features)
   values={1}
   statistic_functions=[calc_mean, calc_stdv]
   data1, data2 = filter_by_feature(data, 'season', values)
   data3, data4 = filter_by_feature(data, 'is_holiday', values)
   features1 = ['hum', 't1', 'cnt']
   features2 = ['t1', 'cnt']
   print("Question 1:")
   print("Summer:")
   statistic_functions2=[calc_covariance]
   print_details(data1, features1, statistic_functions)
   print_joint_details(data1, features2, statistic_functions2, 'Cov(t1, cnt):')
   print("Holiday:")
   print_details(data3, features1, statistic_functions)
   print_joint_details(data3, features2, statistic_functions2, 'Cov(t1, cnt):')
   print("All:")
   print_details(data, features1, statistic_functions)
   print_joint_details(data, features2, statistic_functions2, 'Cov(t1, cnt):')
   print("")
   print("Question 2:")
   values1 = {3}
   data1, data2 = filter_by_feature(data, 'season', values1)
   values1 = {1}
   data3, data4 = filter_by_feature(data1, 'is_holiday', values1)
   print("If t1<=13.0, then:")
   population_statistics('Winter Holiday records:', data3, 't1', 'cnt', 13, False,
                         statistic_functions)
   population_statistics('Winter Weekday records:', data4, 't1', 'cnt', 13, False,
                         statistic_functions)
   data5, data6 = filter_by_feature(data1, 'is_holiday', values1)
   print("If t1>13.0, then:")
   population_statistics('Winter Holiday records:', data5, 't1', 'cnt', 13, True,
                         statistic_functions)
   population_statistics('Winter Weekday records:', data6, 't1', 'cnt', 13, True,
                         statistic_functions)







if __name__ == '__main__':
    main(sys.argv)
