#include <stdio.h>
int main(){
	int h,m;
	int ah,am;
	scanf("%d %d",&h,&m);
	am = (60*h+m-45)%60;
	ah = (60*h+m-45)/60;
	if(h*60+m < 45){
		ah = 23;
		am += 60;
	}
	printf("%d %d",ah,am);
	return 0;
}