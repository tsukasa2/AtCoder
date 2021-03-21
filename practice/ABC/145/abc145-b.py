N = int( input() )
S = str( input() )
 
T_1 = S[ : N // 2 ]
T_2 = S[ N // 2 : ]
 
if T_1 == T_2:
    print( "Yes" )
else:
    print( "No" )