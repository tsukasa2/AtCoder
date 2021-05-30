N = int( input() )
inu = []
inu_RG = []
inu_GB = []
inu_BR = []
for _ in range( 2 * N ):
    a, c = input().split()
    a = int( a )
    inu.append( tuple( ( a, c ) ) )
    if c == "R":
        inu_BR.append( tuple( ( a, c ) ) )
        inu_RG.append( tuple( ( a, c ) ) )
    elif c == "G":
        inu_RG.append( tuple( ( a, c ) ) )
        inu_GB.append( tuple( ( a, c ) ) )
    else:
        inu_GB.append( tuple( ( a, c ) ) )
        inu_BR.append( tuple( ( a, c ) ) )

inu.sort()
inu_RG.sort()
inu_GB.sort()
inu_BR.sort()
RG = []
GB = []
BR = []

for i in range( len( inu_RG ) - 1 ):
    a, c = inu_RG[ i ]
    b, d = inu_RG[ i + 1 ]
    if c != d:
        RG.append( b - a )

for i in range( len( inu_GB ) - 1 ):
    a, c = inu_GB[ i ]
    b, d = inu_GB[ i + 1 ]
    if c != d:
        GB.append( b - a )

for i in range( len( inu_BR ) - 1 ):
    a, c = inu_BR[ i ]
    b, d = inu_BR[ i + 1 ]
    if c != d:
        BR.append( b - a )

from collections import Counter
count = Counter()

for ( _, c ) in inu:
    count[ c ] += 1

if count[ "R" ] % 2 == 0 and count[ "B" ] % 2 == 0:
    print( "0" )
else:
    if count[ "R" ] % 2 == 0:
        if count[ "R" ] == 0:
            print( min( GB ) )
        else:
            print( min( min( GB ), min( RG ) + min( BR ) ) )
    elif count[ "G" ] % 2 == 0:
        if count[ "G" ] == 0:
            print( min( BR ) )
        else:
            print( min( min( BR ), min( GB ) + min( RG ) ) )
    else:
        if count[ "B" ] == 0:
            print( min( RG ) )
        else:
            print( min( min( RG ), min( BR ) + min( GB ) ) )