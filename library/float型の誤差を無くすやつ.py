X_str, Y_str, R_str = map( str, input().split() )

def x10000( n_str ):
    if "." in n_str:
        n_int, n_float = n_str.split( "." )
        n_float = n_float.ljust( 4, "0" )
        return int( n_int + n_float )
    else:
        return int( n_str + "0000" )

X, Y, R = map( x10000, [ X_str, Y_str, R_str ] )
print( X, Y, R )