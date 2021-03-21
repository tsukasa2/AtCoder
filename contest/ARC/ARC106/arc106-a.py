N = int( input() )

# i = 1
# while True:
#     if pow( 3, i ) > pow( 10, 18 ):
#         print( i )
#         break
#     i += 1

# i = 1
# while True:
#     if pow( 5, i ) > pow( 10, 18 ):
#         print( i )
#         break
#     i += 1

a = 1
for i in range( 40 ):
    a *= 3
    b = 1
    for j in range( 30 ):
        b *= 5
        if a + b == N:
            print( i + 1, j + 1 )
            exit()

print( -1 )