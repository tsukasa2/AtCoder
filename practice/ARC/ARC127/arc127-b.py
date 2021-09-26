N, L = map( int, input().split() )

def Base_10_to_n( X, n ):
    if int( X / n ):
        return Base_10_to_n( int( X / n ), n ) + str( X % n )
    return str( X % n )

ans_0 = []
ans_1 = []
ans_2 = []
x = 2 * ( 3 ** ( L - 1 ) ) # 200000...を3進数と解釈したもの
for i in range( N ):
    ans_2.append( Base_10_to_n( x + i, 3 ).zfill( L ) )

for x in ans_2:
    s = ""
    for c in x:
        s += str( ( int( c ) + 1 ) % 3 )

    ans_0.append( s )

    s = ""
    for c in x:
        s += str( ( int( c ) + 2 ) % 3 )

    ans_1.append( s )

print( *ans_0, sep = "\n" )
print( *ans_1, sep = "\n" )
print( *ans_2, sep = "\n" )