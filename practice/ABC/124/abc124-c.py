S = str( input() )

ans_1 = 0
for i, c in enumerate( S ):
    if i % 2 == 0:
        if not c == "0":
            ans_1 += 1
    else:
        if not c == "1":
            ans_1 += 1

ans_2 = 0
for i, c in enumerate( S ):
    if i % 2 == 0:
        if not c == "1":
            ans_2 += 1
    else:
        if not c == "0":
            ans_2 += 1

print( min( ans_1, ans_2 ) )