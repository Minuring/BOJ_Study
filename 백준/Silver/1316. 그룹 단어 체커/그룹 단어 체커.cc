#include <iostream>
#include <cstring>
#include <string> 
using namespace std;
//여기 선언하는 변수,함수들은 std네임스페이스 소속
//namespace에 있는 std클래스에 정의된 함수를 사용하겠다. 

int main(){
	int N, count=0;
	cin >> N;
	string *s = new string[N];
	for(int i=0; i<N; i++){
		int f=1;
		cin >> s[i];
		int len=s[i].length();
		for(int j=0; j<len-1; j++){
			if(s[i][j]==s[i][j+1]) continue;
			if(s[i].find(s[i][j],j+1) != string::npos){
				f = 0;
				break;
			}
		}
		if(f==1) count++;
	}
	printf("%d",count);
	return 0;
}