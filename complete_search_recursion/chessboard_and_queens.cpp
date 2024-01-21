#include<bits/stdc++.h>
using namespace std;
int counter=0;
int column[8];
int diag1[20];
int diag2[20];
int n=4;
int search(int j){
    if(j==n){
        counter+=1;
    }
    else{
        for (int i=0;i<n;i++){
            if (column[i]==1 or diag1[i+j]==1 or diag2[i-j+n-1]==1)
                    continue;
            column[i]=diag1[i+j]=diag2[i-j+n-1]=1;
            search(j+1);
            column[i]=diag1[i+j]=diag2[i-j+n-1]=0;
            
            
        }
    }

}
int main(){
    memset(column,0,sizeof(column));
    memset(diag1,0,sizeof(diag1));
    memset(diag2,0,sizeof(diag2));
    search(0);
    printf("%d",counter);
}