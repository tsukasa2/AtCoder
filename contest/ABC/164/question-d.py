s = input()

cnt = 0
#for c in range( 50 ): #int(s) // 2019 ):
#    d = ( c + 1 ) * 2019
#    for n in range( len( str(s) ) - len( str(d) ) ):
#        if str( d ) in str( s )[n:]:
#            cnt += 1
#            print( d )
#            break

for i in range( len(s) - 3 ):
    for j in range( i+3, len(s) ):
        d = int( s[i:j+1] )
        if d % 2019 == 0:
            cnt += 1
            #print(i,j)

print( cnt )