N = int( input() )
S = [ tuple( map( float, input().split() ) ) for _ in range( N ) ]
T = [ tuple( map( float, input().split() ) ) for _ in range( N ) ]

x, y = S[ 0 ]
S_2 = [ tuple( ( a - x, b - y ) ) for ( a, b ) in S ]
S_2.sort()

def heikou( S, T, N ):
    for i in range( N ):
        x, y = T[ i ]
        T_1 = [ tuple( ( a - x, b - y ) ) for ( a, b ) in T ]
        T_1.sort()
        if S == T_1:
            return True
    
    return False

x, y = 0, 0
# 0回転
T_2 = T
T_2.sort()
if heikou( S_2, T_2, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a - 3 * b ) / 5, ( 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a - 4 * b ) / 5, ( 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a + 3 * b ) / 5, ( - 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a + 4 * b ) / 5, ( - 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

# pi / 2回転
T_2 = [ tuple( ( -( b - y ), a - x ) ) for ( a, b ) in T ]
T_2.sort()
if heikou( S_2, T_2, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a - 3 * b ) / 5, ( 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a - 4 * b ) / 5, ( 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a + 3 * b ) / 5, ( - 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a + 4 * b ) / 5, ( - 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

# pi回転
T_2 = [ tuple( ( -( a - x ), -( b - y ) ) ) for ( a, b ) in T ]
T_2.sort()
if heikou( S_2, T_2, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a - 3 * b ) / 5, ( 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a - 4 * b ) / 5, ( 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a + 3 * b ) / 5, ( - 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a + 4 * b ) / 5, ( - 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

# 3 * pi / 2回転
T_2 = [ tuple( ( b - y, -( a - x ) ) ) for ( a, b ) in T ]
T_2.sort()
if heikou( S_2, T_2, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a - 3 * b ) / 5, ( 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a - 4 * b ) / 5, ( 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 4 * a + 3 * b ) / 5, ( - 3 * a + 4 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

T_3 = [ tuple( ( ( 3 * a + 4 * b ) / 5, ( - 4 * a + 3 * b ) / 5  ) ) for ( a, b ) in T_2 ]
T_3.sort()
if heikou( S_2, T_3, N ):
    print( "Yes" )
    exit()

print( "No" )