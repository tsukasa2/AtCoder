h, w, k = map( int, input().split() )
c = []
for _ in range( h ):
    c_i = str( input() )
    c.append( c_i )

ans = 0

c_h = [ 0 for _ in range( h ) ] # c[ i ] = i行目にある#の個数
c_w = [ 0 for _ in range( w ) ] # c[ j ] = j列目にある#の個数
all_black = 0

for i in range( h ):
    for j in range( w ):
        if c[ i ][ j ] == "#":
            c_h[ i ] += 1
            c_w[ j ] += 1
            all_black += 1

def count_black( list_h, list_w ):
    cnt = all_black
    for i in list_h:
        cnt -= c_h[ i ]
    for j in list_w:
        cnt -= c_w[ j ]
    for i in list_h:
        for j in list_w:
            if c[ i ][ j ] == "#":
                cnt += 1
    return cnt

def solve( i, list_h, j, list_w ):
    if i < h:
        solve( i + 1, list_h, j, list_w )
        solve( i + 1, list_h + [ i ], j, list_w )
    else:
        if j < w:
            solve( i, list_h, j + 1, list_w )
            solve( i, list_h, j + 1, list_w + [ j ] )
        else:
            if k == count_black( list_h, list_w ):
                global ans
                ans += 1

solve( 0, [], 0, [] )
print( ans )


# def horizonal( j, cnt ):
#     global ans
#     if cnt == k:
#         ans += 1
#     j += 1
#     if j == 6:
#         return
#     horizonal( j, cnt )
#     horizonal( j, cnt - c_w[ j ] )

# def vertical( i, cnt ):
#     for j in range( w ):
        