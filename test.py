schema_col_list = ["col1","col2","col3","col4","col5","col6","col7","col8","col9"]
# schema_col_list = ["col6","col7"]

rows = []
with open("hello.csv", 'r') as f:
    rows = f.readlines()
rows = [row.split('\n')[0] for row in rows]
rows = [row.split(',') for row in rows]
# print(rows)

def normalize(schema_col_list, rows):
    header_row = rows[0]
    missing_cols = list(set(schema_col_list) - set(header_row))
    missing_data = [None]*(len(missing_cols))
    extra_cols = [c for c in header_row if c not in schema_col_list]
    data_rows = [row + [d for d in missing_data] for row in rows[1:]]
    header_row.extend(missing_cols)
    final_col_order = schema_col_list + extra_cols
    exchange_map = [[i, header_row.index(c)] for i, c in enumerate(final_col_order)]
    print(header_row)
    print(exchange_map)
    print(final_col_order)
    final_data_rows = []
    for row in data_rows:
        row_temp = [row[j] for i, j in exchange_map]
        print(row_temp)
    print(extra_cols)
    print(missing_cols)
    return rows


if __name__ == "__main__":
    rows_1 = normalize(schema_col_list, rows)
    # print(rows_1)
