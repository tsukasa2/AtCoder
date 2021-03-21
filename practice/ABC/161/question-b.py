n, m = input().split()
a = input().split()
vote = 0
cnt = 0

for i in range( len(a) ):
    vote += int( a[i] )

for i in range( len(a) ):
    if int( a[i] ) >= vote / ( 4 * int( m ) ):
        cnt += 1

if cnt >= int( m ):
    print("Yes")
else:
    print("No")