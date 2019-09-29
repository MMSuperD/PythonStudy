
# 行号
row = 1

while row <= 9:

    # 列号
    col = 1
    while col <= row:
        print("%d * %d = %d" %(row,col,row * col),end="\t")
        col += 1
    print(end="\n")
    row += 1
