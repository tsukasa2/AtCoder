k = int( input() )

def ajdacent( a ):
    if a == 0:
        return [0, 1]
    elif a > 0 and a < 9:
        return [a-1, a, a+1]
    elif a == 9:
        return [8, 9]
    else:
        return []

#first_digitで始まるn桁のルンルン数の個数を返す
def lun_count( n, first_digit ):
    if n < 1:
        return False
    elif n == 1:
        return 1
    elif n == 2:
        return len( ajdacent( first_digit ) )
    else:
        count = 0
        for second_digit in ajdacent( first_digit ):
            count += lun_count( n-1, second_digit )
        return count
        
#print( lun_count(k, 1) )

#以下カンニング

lunlun_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lunlun_maker( lun_num, lun_list ):
    if lun_num % 10 == 0:
        lun_list.append( lun_num * 10  )
        lun_list.append( lun_num * 10 + 1 )
    elif lun_num % 10 == 9:
        lun_list.append( lun_num * 10 + 8 )
        lun_list.append( lun_num * 10 + 9 )
    else:
        lun_list.append( lun_num * 10 + ( lun_num % 10 - 1 ) )
        lun_list.append( lun_num * 10 + ( lun_num % 10 ) )
        lun_list.append( lun_num * 10 + ( lun_num % 10 + 1 ) )

i = 0
while len( lunlun_numbers ) < 100000:
    lunlun_maker( lunlun_numbers[i], lunlun_numbers )
    i += 1

print( lunlun_numbers[ k - 1 ] )