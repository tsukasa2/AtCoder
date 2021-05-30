N, K = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

AB.sort()

taro = 0
money = K

for ( a, b ) in AB:
    if taro + money < a:
        taro += money
        money = 0
        break
    else:
        taro += a
        money += -a + b

print( taro + money )