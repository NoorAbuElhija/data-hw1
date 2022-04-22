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



def main(argv):

   features = ['hum', 't1', 'cnt', 'season', 'is_holiday']

   path = 'C:\\Users\\noor2\\OneDrive\\Desktop\\data\\london.csv'

   data = load_data(path, features)
   values={1}
   statistic_functions=[calc_mean, calc_stdv]
   data1, data2 = filter_by_feature(data, 'season', values)
   data3, data4 = filter_by_feature(data, 'is_holiday', values)
   features = ['hum', 't1', 'cnt']
   features2 = ['t1', 'cnt']
   print("summer:")
   statistic_functions2=[calc_covariance]
   print_details(data1, features, statistic_functions)
   print_joint_details(data3, features2, statistic_functions2, 'Cov(t1, cnt)')
   print("holiday:")
   print_details(data3, features, statistic_functions)
   print_joint_details(data1, features2, statistic_functions2, 'Cov(t1, cnt)')
   print("All:")
   print_details(data, features, statistic_functions)
   print_joint_details(data, features2, statistic_functions2, 'Cov(t1, cnt)')


if __name__ == '__main__':
    main(sys.argv)
