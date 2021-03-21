#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    char s[200000], t[200000];
    int i, j, k, d, cnt;
    scanf("%s", &s);
    cnt = 0;
    for( i=0; i<strlen(s)-3; i++ ){
        for( j=i+3; j<strlen(s); j++ ){
            d = 0;
            for( k=0; k<j-i; k++ ){
                d += pow(10,k) * s[k];
                printf("%d\n", d);
            }
            if( d%2019==0 ){
                cnt++;
            }     
        }
    }
    printf("%d\n", cnt);
    return 0;
}