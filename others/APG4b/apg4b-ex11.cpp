#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, A, B, i, x;
    string op;
    bool err_flag = false;

    cin >> N >> A;

    x = A;
    for( i = 0; i < N; i++ ){
        cin >> op >> B;
        if( op == "+" ){
            x += B;
        }else if( op == "-" ){
            x -= B;
        }else if( op == "*" ){
            x *= B;
        }else if( op == "/" ){
            if( B == 0 ){
                if( !err_flag ){
                    cout << "error" << endl;
                }
                err_flag = true;
            }else{
                x /= B;
            }
        }
        if( !err_flag ){
            cout << i + 1 << ":" << x << endl;
        }
    }
}