W, H, x, y = map( int, input().split() )

# 重心を通る線で2等分した面積が答え
# ( x, y )が重心のときは答えが無数にある
if x == W / 2 and y == H / 2:
    print( W * H / 2, 1 )
else:
    print( W * H / 2, 0 )