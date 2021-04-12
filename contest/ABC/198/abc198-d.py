import itertools

S_1 = str( input() )
S_2 = str( input() )
S_3 = str( input() )

dic = {}
n = 0
for c in S_1 + S_2 + S_3:
    if c in dic.keys():
        continue
    else:
        dic[ c ] = n
        n += 1

if n > 10:
    print( "UNSOLVABLE" )
    exit()

d = ( "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" )
for p in itertools.permutations( d, n ):
    if p[ dic[ S_1[ 0 ] ] ] == "0" or p[ dic[ S_2[ 0 ] ] ] == "0" or p[ dic[ S_3[ 0 ] ] ] == "0":
        continue

    T_1, T_2, T_3 = "", "", ""
    for c in S_1:
        T_1 += p[ dic[ c ] ]
    for c in S_2:
        T_2 += p[ dic[ c ] ]
    for c in S_3:
        T_3 += p[ dic[ c ] ]
    
    if int( T_3 ) == int( T_1 ) + int( T_2 ):
        print( T_1 )
        print( T_2 )
        print( T_3 )
        break
else:
    print( "UNSOLVABLE" )