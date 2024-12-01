import pandas as pd
import numpy as np
from collections import Counter

def main():
    df = pd.read_csv("./Day1/file.csv", header=None, delimiter='   ')
    df0 = df[0].sort_values()
    df1 = df[1].sort_values()
    a = np.sum(np.abs(df0.to_numpy() - df1.to_numpy()))
    print("Answer to part 1: ", a)
    # Part 2
    c0 = Counter(df0.to_numpy())
    c1 = Counter(df1.to_numpy())

    df2 = pd.concat([pd.Series(c0), pd.Series(c1)], axis=1)
    df2 = df2.fillna(0)
    b = np.sum(df2.index.T * df2[0] * df2[1])
    print("Answer to part 2: ", b)

if __name__ == '__main__':
    main()