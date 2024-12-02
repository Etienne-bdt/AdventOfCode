import numpy as np
import pandas as pd

def monotonic(df):
    increasing = df.apply(lambda row: row[row.notna()].is_monotonic_increasing, axis=1)
    decreasing = df.apply(lambda row: row[row.notna()].is_monotonic_decreasing, axis=1)
    return df[increasing | decreasing]
    
def monotonic2(df):
    def is_almost_monotonic(row):
        row = row.dropna()
        if (row.is_monotonic_increasing or row.is_monotonic_decreasing) and row_distance(row):
            return True
        for i in range(len(row)):
            temp_row = row.drop(row.index[i])
            if (temp_row.is_monotonic_increasing or temp_row.is_monotonic_decreasing) and row_distance(temp_row):
                return True
        return False

    almost_increasing = df.apply(is_almost_monotonic, axis=1)
    return df[almost_increasing]

def row_distance(row):
    row = row.dropna()
    row_pad = row[1:].reset_index(drop=True)
    row_sel = row[:-1].reset_index(drop=True)
    sub = row_sel.sub(row_pad).abs()
    maxv = sub.max()
    minv = sub.min()
    no_var = sub[sub==0].count() ==0
    return (maxv <=3 and minv>0) and no_var 

def main():
    df = pd.read_csv("./Day2/file.csv", header=None, delimiter=' ')

    # Part 1
    #check if row is monotonic

    # 1 3 2 should become 1 2 3 
    # 4 5 6 should stay the same


    mon = monotonic(df)

    safe = mon.apply(lambda row: row_distance(row[row.notna()]), axis=1)

    print("Answer to part 1: ", safe.sum())

    # Part 2
    safe2 = monotonic2(df)
    print("Answer to part 2: ", len(safe2))

if __name__ == '__main__':
    main()