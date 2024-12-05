import polars as pl

def rule_check(ruleset_dict, odr):
    for j in range(len(odr)):
        rule1 = ruleset_dict.get(odr[j], {}).get('rule1', set())
        rule2 = ruleset_dict.get(odr[j], {}).get('rule2', set())
        for k in range(j):
            if odr[k] in rule2:
                return False
        for k in range(j+1, len(odr)):
            if odr[k] in rule1:
                return False
    return True

def main():
    df = pl.read_csv("./Day5/file.csv", has_header=False, separator='|', infer_schema_length=10000)
    df1 = df.filter(df['column_1'].is_not_null() & df['column_2'].is_not_null())
    df1 = df1.with_columns(pl.col("column_1").cast(pl.Int64))
    df2 = df.filter(df['column_1'].is_not_null() & df['column_2'].is_null())

    # Create a dictionary for fast lookup
    ruleset_dict = {}
    for row in df1.iter_rows(named=True):
        col1 = row['column_1']
        col2 = row['column_2']
        if col1 not in ruleset_dict:
            ruleset_dict[col1] = {'rule1': set(), 'rule2': set()}
        if col2 not in ruleset_dict:
            ruleset_dict[col2] = {'rule1': set(), 'rule2': set()}
        ruleset_dict[col1]['rule2'].add(col2)
        ruleset_dict[col2]['rule1'].add(col1)

    # Apply rule_check to each row of df2
    sum = 0
    for row in df2.iter_rows(named=True):
        odr = row['column_1']
        odr_list = odr.split(',')
        odr = [int(i) for i in odr_list]
        if rule_check(ruleset_dict, odr):
            sum += odr[len(odr) // 2]

    print("Answer for part 1:", sum)

if __name__ == "__main__":
    main()
