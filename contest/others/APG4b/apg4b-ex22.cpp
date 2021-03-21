#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;

    vector< pair< int, int > > b_a( N );
    for( int i = 0; i < N; i++ ){
        cin >> b_a.at( i ).second >> b_a.at( i ).first;
    }

    sort( b_a.begin(), b_a.end() );

    for( int i = 0; i < N; i++ ){
        cout << b_a.at( i ).second << " " << b_a.at( i ).first << endl;
    }
}