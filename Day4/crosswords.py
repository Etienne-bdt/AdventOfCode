import polars as pl
import re

def find_XorS(df: pl.DataFrame):
    sum = 0
    i=0
    while len(df)>0:
        for j in range(len(df['column_1'][i])):
            try:
                if df['column_1'][i][j] == 'X':
                    if df['column_1'][i+1][j] == 'M' and df['column_1'][i+2][j] == 'A' and df['column_1'][i+3][j] == 'S':
                        sum += 1
                    if (j-1)>=0 and (j-2)>=0 and (j-3)>=0 and df['column_1'][i+1][j-1] == 'M' and df['column_1'][i+2][j-2] == 'A' and df['column_1'][i+3][j-3] == 'S':
                        sum += 1
                    if df['column_1'][i+1][j+1] == 'M' and df['column_1'][i+2][j+2] == 'A' and df['column_1'][i+3][j+3] == 'S':
                        sum += 1
                if df['column_1'][i][j] == 'S':
                    if df['column_1'][i+1][j] == 'A' and df['column_1'][i+2][j] == 'M' and df['column_1'][i+3][j] == 'X':
                        sum += 1
                    if (j-1)>=0 and (j-2)>=0 and (j-3)>=0 and df['column_1'][i+1][j-1] == 'A' and df['column_1'][i+2][j-2] == 'M' and df['column_1'][i+3][j-3] == 'X':
                        sum += 1
                    if df['column_1'][i+1][j+1] == 'A' and df['column_1'][i+2][j+2] == 'M' and df['column_1'][i+3][j+3] == 'X':
                        sum += 1
            except IndexError:
                continue
        df = df.slice(1, len(df))

    return sum

def find_X_MAS(df: pl.DataFrame):
    sum = 0
    i=0
    while len(df)>0:
        for j in range(len(df['column_1'][i])):
            try:
                if df['column_1'][i][j] == 'M':
                    if df['column_1'][i+1][j+1] == 'A' and df['column_1'][i+2][j+2] == 'S':
                        if df['column_1'][i+2][j] == 'S' and df['column_1'][i][j+2] == 'M':
                            sum += 1
                        elif df['column_1'][i+2][j] == 'M' and df['column_1'][i][j+2] == 'S':
                            sum += 1
                if df['column_1'][i][j] == 'S':
                    if df['column_1'][i+1][j+1] == 'A' and df['column_1'][i+2][j+2] == 'M':
                        if df['column_1'][i+2][j] == 'S' and df['column_1'][i][j+2] == 'M':
                            sum += 1
                        elif df['column_1'][i+2][j] == 'M' and df['column_1'][i][j+2] == 'S':
                            sum += 1
            except IndexError:
                continue
        df = df.slice(1, len(df))
    return sum



def main():
    df = pl.read_csv("./Day4/file.csv", has_header=False)
    horiz = df['column_1'].str.count_matches("XMAS")
    horiz += df['column_1'].str.count_matches("SAMX")
    horiz = horiz.sum()

    others = find_XorS(df)
    print("Answer for part 1: ", horiz+others)
    print("Answer for part 2: ", find_X_MAS(df))

if __name__ == "__main__":
    main()
