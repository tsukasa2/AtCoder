N = str( input() )
K = int( input() )

def solve( N, K ):
    N = N.lstrip( "0" )
    if K > len( N ):
        return 0
    
    if K == 1:
        return int( N[ 0 ] ) + 9 * ( len( N ) - 1 )
    elif K == 2:
        res = 0
        res += solve( N[ 1 : ], 1 )
            # 上1桁をNと同じにするとき
        res += ( int( N[ 0 ] ) - 1 ) * 9 * ( len( N ) - 1 )
            # 上1桁をNのものより小さく0より大きくするとき
        res += solve( "9" * ( len( N ) - 1 ), 2 )
            # 上1桁を0にするとき
        return res
    elif K == 3:
        res = 0
        res += solve( N[ 1 : ], 2 )
            # 上1桁をNと同じにするとき
        res += ( int( N[ 0 ] ) - 1 ) * 81 * ( len( N ) - 1 ) * ( len( N ) - 2 ) // 2
            # 上1桁をNのものより小さく0より大きくするとき
        res += solve( "9" * ( len( N ) - 1 ), 3 )
            # 上1桁を0にするとき
        return res

    return 0

print( solve( N, K ) )