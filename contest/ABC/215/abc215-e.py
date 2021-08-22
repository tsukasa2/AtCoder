N = int( input() )
S = str( input() )

MOD = 998244353

chars = "ABCDEFGHIJ"
DP = [ { 
    "A" : [ 0, 0, 0 ],
    "B" : [ 0, 0, 0 ],
    "C" : [ 0, 0, 0 ],
    "D" : [ 0, 0, 0 ],
    "E" : [ 0, 0, 0 ],
    "F" : [ 0, 0, 0 ],
    "G" : [ 0, 0, 0 ],
    "H" : [ 0, 0, 0 ],
    "I" : [ 0, 0, 0 ],
    "J" : [ 0, 0, 0 ]
} ]

DP[ 0 ][ S[ 0 ] ][ 0 ] = 1
for i in range( 1, N ):
    for c in chars:
        x, y, z = DP[ i - 1 ][ c ]
        if c == S[ i ]:
            DP[ i ][ c ][ 0 ] = ( x + z ) * 2
            DP[ i ][ c ][ 1 ] = y
            DP[ i ][ c ][ 2 ] = z
        else:
            DP[ i ][ c ][ 0 ] = x
            DP[ i ][ c ][ 1 ] = y + z