# a, b = map( int, input().split() )

# x_8 = ( a * 100 // 8 )
# for x in range( x_8, x_8 + 13 ):
#     if x // 10 == b:
#         print( x )
#         exit()
# print( -1 ) 

a, b = map( int, input().split() )

for n in range( 1, 1001 ):
    if int( n * 0.08 ) == a and int( n * 0.1 ) == b:
        print( n )
        exit()
print( -1 )