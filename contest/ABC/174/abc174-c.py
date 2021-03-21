k = int( input() )

# a = 7
# for _ in range( 30 ):
#     print( a % k )
#     a = 10 * a + 7

rem_list = []
first_rem = 7 % k
a = 7
cnt = 0
while True:
    r = a % k
    cnt += 1
    if r == 0:
        print( cnt )
        break
    elif cnt > 2 and cnt > k:
        print( -1 )
        break
    else:
        a = ( 10 * r + 7 ) % k