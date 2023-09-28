#include <stdio.h>
int main(){
	int N;
	scanf("%d",&N);
	int newnum=N, n1,n10,count=0;
	while(1){
		n1 = newnum%10;
		n10 = newnum/10;
		newnum= n1*10+(n10+n1)%10;
		count++;
	//	printf("%d\n",newnum);
		if(newnum==N)break;
		
	}
	printf("%d",count);
	return 0;
} 