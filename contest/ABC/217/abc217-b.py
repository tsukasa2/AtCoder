S_1 = str( input() )
S_2 = str( input() )
S_3 = str( input() )

if not "ABC" in [ S_1, S_2, S_3 ]:
    print( "ABC" )
elif not "ARC" in [ S_1, S_2, S_3 ]:
    print( "ARC" )
elif not "AGC" in [ S_1, S_2, S_3 ]:
    print( "AGC" )
else:
    print( "AHC" )