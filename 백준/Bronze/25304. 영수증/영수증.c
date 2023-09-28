#include <stdio.h>
 int main(){
 	int total, kinds, price, num, sum=0;
 	scanf("%d %d", &total, &kinds);
	for(int i=0; i<kinds; i++){
		scanf("%d %d", &price, &num);
		sum += price*num;
	}
	
	sum==total ? printf("Yes") : printf("No");
	return 0;
 }