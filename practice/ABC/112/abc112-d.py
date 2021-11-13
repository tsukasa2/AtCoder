def make_divisors( n ):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append( i )
            if i != n // i:
                upper_divisors.append( n // i )
        i += 1
    return lower_divisors + upper_divisors[ ::-1 ]

N, M = map( int, input().split() )

divs = make_divisors( M )
divs.sort( reverse = True )
for d in divs:
    if M // d >= N:
        print( d )
        break