a = []
for _ in range( 3 ):
    a.append( list( map( int, input().split() ) ) )

n = int( input() )
b = []
for _ in range( n ):
    b.append( int( input() ) )

bingo = [ [ False ] * 3 for _ in range( 3 ) ]

for i in range( 3 ):
    for j in range( 3 ):
        if a[ i ][ j ] in b:
            bingo[ i ][ j ] = True

for i in range( 3 ):
    if bingo[ i ][ 0 ] and bingo[ i ][ 1 ] and bingo[ i ][ 2 ]:
        print( "Yes" )
        exit()

for j in range( 3 ):
    if bingo[ 0 ][ j ] and bingo[ 1 ][ j ] and bingo[ 2 ][ j ]:
        print( "Yes" )
        exit()

if bingo[ 0 ][ 0 ] and bingo[ 1 ][ 1 ] and bingo[ 2 ][ 2 ]:
    print( "Yes" )
    exit()

if bingo[ 0 ][ 2 ] and bingo[ 1 ][ 1 ] and bingo[ 2 ][ 0 ]:
    print( "Yes" )
    exit()

print("No")