S = str( input() )

def is_month( x ):
    return x > 0 and x < 13

front = int( S[ 0 : 2 ] )
back = int( S[ 2 : 4 ] )

if is_month( front ) and is_month( back ):
    print( "AMBIGUOUS" )
elif is_month( front ):
    print( "MMYY" )
elif is_month( back ):
    print( "YYMM" )
else:
    print( "NA" )