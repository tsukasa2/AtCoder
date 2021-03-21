# n = int( input() )
# a = []
# b = []
# for _ in range( n ):
#     a_i, b_i = map( int, input().split() )
#     a.append( a )
#     b.append( b )
# MOD = 1000000007

# fact = [ 1, 1 ]
# inv = [ 0, 1 ]
# inv_fact = [ 1, 1 ]
# for k in range( 2, n+1 ):
#     fact.append( fact[-1] * k % MOD )
#     inv.append( ( - inv[ MOD % k ] * ( MOD // k ) ) % MOD )
#     inv_fact.append( inv_fact[-1] * inv[-1] % MOD )

# def cmb( k, l ):
#     return fact[k] * inv_fact[k-l] * inv_fact[l]

# ans = 1

# for i in range( n ):

####以下カンニング####
import math

n = int( input() )
a = []
b = []
for _ in range( n ):
    a_i, b_i = map( int, input().split() )
    a.append( a_i )
    b.append( b_i )
MOD = 1000000007

def key_gen( a_i, b_i ):
    if a_i == 0 and b_i == 0:
        return "0/0"
    elif a_i == 0:
        return "N/0"
    elif b_i == 0:
        return "0/N"
    else:
        if a_i * b_i < 0:
            sign = "-"
        else:
            sign = ""
        m = math.gcd( a_i, b_i )
        a_i = abs( a_i ) // m
        b_i = abs( b_i ) // m
        key = sign + str( b_i ) + "/" + str( a_i )
        return key

hate = {} # { "-b/a" : a / b == - b[i] / a[i] なるiの個数 }

for i in range( n ):
    a_i = a[i]
    b_i = b[i]

    key = key_gen( a_i, b_i )
    try:
        hate[ key ] += 1
    except KeyError:
        hate[ key ] = 1
    
print( hate )

iwashi = 1
pow2 = [1]
for i in range( n ):
    iwashi = iwashi * 2 % MOD
    pow2.append( iwashi )



