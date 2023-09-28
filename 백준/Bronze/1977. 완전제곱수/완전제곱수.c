#include <stdio.h>
#include <math.h>
int main(){
	signed int m,n, min=0, sum=0;
	scanf("%d %d",&m,&n);
	for(int i=0; i*i<=n; i++){
		if(i*i>=m){
			if(min==0) min=i*i;
			sum += i*i;
		}
	}
	
	if(sum==0){
		printf("-1");
	}else{
		printf("%d\n%d",sum,min);
	}
	return 0;
}