#include <stdio.h>
int main(){
	int n1,n2,n3,reward;
	scanf("%d %d %d",&n1,&n2,&n3);
	if(n1==n2 && n1==n3){
		reward = 10000+n1*1000;
	}else if(n1==n2 || n2==n3 || n3==n1){
		reward = (n1==n2||n2==n3) ? 1000+n2*100 : 1000+n1*100;
	}else{
		if(n1>=n2 && n1>=n3) reward = n1*100;
		if(n2>=n1 && n2>=n3) reward = n2*100;
		if(n3>=n1 && n3>=n2) reward = n3*100;
	}
	
	printf("%d",reward);
	return 0;
}