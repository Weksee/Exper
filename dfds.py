file = open('9_8467.csv')
counter = 0
for row in file:
    if row.strip():  
        row = list(map(int, row.strip().split('"')))
        dlina = len(set(row))
        max_row = max(row)
        min_row = min(row)
        sum_row = sum(row) - (max_row + min_row)
        if (dlina == 5) != ((max_row + min_row) * 2 < sum_row):
            counter += 1
print(counter)

