N = int( input() )
segments = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

def judge( seg_1, seg_2 ):
    t_1, l_1, r_1 = seg_1
    t_2, l_2, r_2 = seg_2
    if l_1 < l_2 and l_2 < r_1:
        return True
    elif l_1 < r_2 and r_2 < r_1:
        return True
    elif l_2 < l_1 and l_1 < r_2:
        return True
    elif l_2 < r_1 and r_1 < r_2:
        return True
    elif l_1 == l_2 or r_1 == r_2:
        return True
    elif r_1 == l_2:
        if t_1 == 1 or t_1 == 3:
            if t_2 == 1 or t_2 == 2:
                return True
    elif l_1 == r_2:
        if t_1 == 1 or t_1 == 2:
            if t_2 == 1 or t_2 == 3:
                return True
    else:
        return False

ans = 0
for i in range( N - 1 ):
    for j in range( i + 1, N ):
        if judge( segments[ i ], segments[ j ] ):
            ans += 1
        # print( i, j, ans )

print( ans )