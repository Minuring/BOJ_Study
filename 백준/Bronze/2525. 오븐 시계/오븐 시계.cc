#include <stdio.h>
int main(){
	int nowH,nowM,cookT;
	scanf("%d %d %d",&nowH,&nowM,&cookT);
	int finH,finM = nowH*60 + nowM + cookT;
	finH = finM/60>=24 ? finM/60-24 : finM/60;
	finM = finM%60;
	printf("%d %d",finH,finM);
	return 0;
}