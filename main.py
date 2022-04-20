# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import sys
import pandas as pd



def main(argv):

   features = ['hum', 't1', 'cnt', 'season', 'is_holiday']
   print(222)
   path = 'C:\\Users\\noor2\\OneDrive\\Desktop\\data\\london.csv'
   print(333)
   data = load_data(path, features)
   values={82, 93, 75}
   data1, data2 = filter_by_feature(data, 'hum', values)
   df2=pd.DataFrame(data2)
   df1=pd.DataFrame(data1)
   print(data1)
   print(data2)


if __name__ == '__main__':
    main(sys.argv)
