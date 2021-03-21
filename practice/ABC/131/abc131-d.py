N = int( input() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

time = 0
schedule = []
for ( A, B ) in AB:
    schedule.append( ( B, -A ) )

schedule.sort()

for ( B, A ) in schedule:
    A *= -1
    time += A
    if time > B:
        print( "No" )
        break
else:
    print( "Yes" )