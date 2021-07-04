N = int( input() )
S = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]
T = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

if N == 1:
    print( "Yes" )
    exit()

def kyori( A, B ):
    a_x, a_y = A
    b_x, b_y = B
    x = a_x - b_x
    y = a_y - b_y
    return x * x + y * y

def gaiseki( A, B ):
    a_x, a_y = A
    b_x, b_y = B
    return a_x * b_y - a_y * b_x

c = S[ 0 ]
s_1 = ( S[ 1 ][ 0 ] - c[ 0 ], S[ 1 ][ 1 ] - c[ 1 ] )
gaisekis_S = [ 
    (
        kyori( ( s[ 0 ] - c[ 0 ], s[ 1 ] - c[ 1 ] ), s_1 ),
        gaiseki( ( s[ 0 ] - c[ 0 ], s[ 1 ] - c[ 1 ] ), s_1 ) 
    ) for s in S 
]

ans = False

import itertools

for t_1, t_2 in itertools.permutations( T, 2 ):
    t_2 = ( t_2[ 0 ] - t_1[ 0 ], t_2[ 1 ] - t_1[ 1 ] )
    gaisekis_T = [ 
        (
            kyori( ( t[ 0 ] - t_1[ 0 ], t[ 1 ] - t_1[ 1 ] ), t_2 ),
            gaiseki( ( t[ 0 ] - t_1[ 0 ], t[ 1 ] - t_1[ 1 ] ), t_2 ) 
        ) for t in T 
    ]
    if set( gaisekis_S ) == set( gaisekis_T ):
        # print( t_1, t_2 )
        # print( gaisekis_S )
        # print( gaisekis_T )
        ans = True

if ans:
    print( "Yes" )
else:
    print( "No" )