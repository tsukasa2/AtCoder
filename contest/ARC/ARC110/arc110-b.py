N = int( input() )
T = str( input() )

if T == "1":
    print( 2 * ( 10 ** 10 ) )
    exit()
elif T == "0" or T == "10" or T == "11":
    print( 10 ** 10 )
    exit()
elif T == "01":
    print( 10 ** 10 - 1 )
    exit()
elif T == "00" or T == "010":
    print( 0 )
    exit()

if T[ : 2 ] == "11":
    k = 0
elif T[ : 2 ] == "01":
    k = 1
elif T[ : 2 ] == "10":
    k = 2
else:
    print( 0 )
    exit()

if T[ -2 : ] != "10" and T[ -2 : ] != "01" and T[ -2 : ] != "11":
    print( 0 )
    exit()

while k + 3 <= N:
    if T[ k : k + 3 ] != "110":
        print( 0 )
        exit()
    k += 3

zero_count = 0
for k in range( N ):
    if T[ k ] == "0":
        zero_count += 1
if T[ -1 ] == "0":
    blocks = zero_count
else:
    blocks = zero_count + 1
print( 10 ** 10 - ( blocks - 1 ) )