import polars as pl
import numpy as np

def rule_check(ruleset,odr):
    for j in range(len(odr)):
        rule1 = ruleset.filter(pl.col("column_2") == odr[j])['column_1']
        rule2 = ruleset.filter(pl.col("column_1") == odr[j])['column_2']
        for k in range(j):
            if odr[k] in rule2:
                return False
        for k in range(j+1,len(odr)):
            if odr[k] in rule1:
                return False
    return True

def main():
    df = pl.read_csv("./Day5/file.csv", has_header=False, separator='|', infer_schema_length=10000)
    df1 = df.filter(df['column_1'].is_not_null() & df['column_2'].is_not_null())
    df1 = df1.with_columns(pl.col("column_1").cast(pl.Int64))
    df2 = df.filter(df['column_1'].is_not_null() & df['column_2'].is_null())
    
    # Apply rule_check to each row of df2
    results = []
    sum=0
    for row in df2.iter_rows(named=True):
        odr = row['column_1']
        odr_list = odr.split(',')
        odr = [int(i) for i in odr_list]
        if rule_check(df1, odr):
            #sum takes the mid result of results
            sum += odr[len(odr)//2]
    
    print(sum)

if __name__ == "__main__":
    main()
