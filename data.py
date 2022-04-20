import pandas as pd

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
