def count_rows_1s(llist):
    count_rows = 0
    for row in llist:
        count_1s = 0
        for element in row:
            if element == 1:
                count_1s += 1
        if count_1s == len(row):
            count_rows += 1
    return count_rows


llist =  [ [ 1, 1, 1, 1, 1, 1, 1],
           [ 0, 0, 1, 0, 0, 1, 0],
           [ 0, 0, 0, 0, 1, 1, 0],
           [ 0, 0, 1, 0, 0, 0, 0],
           [ 1, 1, 1, 1, 1, 1, 1] ]
print(count_rows_1s(llist)) # 2