T = int( input() )
case = [ int( input() ) for _ in range( T ) ]

def judge( K, case_i ):
    tmp_1 = K
    tmp_2 = 3 * K
    d = 10
    for _ in range( 18 ):
        if tmp_1 < case_i and case_i < tmp_2:
            print( K, d // 10, tmp_1, case_i, tmp_2 )
            return True
        
        tmp_1 += d
        tmp_2 += 3 * K * d
        d *= 10
    
    return False

for case_i in case:
    l = 0
    r = case_i
    while r - l > 1:
        m = ( l + r ) // 2
        # print( case_i, m, judge( m, case_i ) )
        if judge( m, case_i ):
            r = m
        else:
            l = m

    print( r )