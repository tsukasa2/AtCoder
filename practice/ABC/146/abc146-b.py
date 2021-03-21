N = int( input() )
S = str( input() )

alphabet = [ "A", "B", "C", "D", "E", "F", "G", 
    "H", "I", "J", "K", "L", "M", "N", "O", "P", 
    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

reverse_alphabet = {}
for i in range( 26 ):
    reverse_alphabet[ alphabet[ i ] ] = i

def rotate( c, n ):
    return alphabet[ ( reverse_alphabet[ c ] + n ) % 26 ]

ans = ""
for c in S:
    ans += rotate( c, N )

print( ans )