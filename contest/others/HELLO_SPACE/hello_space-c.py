N = int( input() )
ABCDE = [ tuple( map( int, input().split() ) ) ]

def team_power( P, Q, R ):
    a = max( [ P[ 0 ], Q[ 0 ], R[ 0 ] ] )
    b = max( [ P[ 1 ], Q[ 1 ], R[ 1 ] ] )
    c = max( [ P[ 2 ], Q[ 2 ], R[ 2 ] ] )
    d = max( [ P[ 3 ], Q[ 3 ], R[ 3 ] ] )
    e = max( [ P[ 4 ], Q[ 4 ], R[ 4 ] ] )
    return min( [ a, b, c, d, e ] )

