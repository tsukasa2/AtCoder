n, k = map( int, input().split() )
a = list( map( int, input().split() ) )

a.sort()

nega = 0
zero = 0
posi = 0

for x in a:
    if x < 0:
        nega += 1
    elif x == 0:
        zero += 1
    else:
        posi += 1

