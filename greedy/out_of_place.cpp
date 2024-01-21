#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    int a[100]={0,};
    
    int b[100]={0,};
    for(int i=0;i<t;i++){
        cin >> a[i];
        b[i]=a[i];
    }
    sort(b,b+t);
    int swaps=0;
    for(int i=0;i<t;i++){
        if(b[i]!=a[i]) swaps++;
    }
    cout << swaps-1 << '\n';

}