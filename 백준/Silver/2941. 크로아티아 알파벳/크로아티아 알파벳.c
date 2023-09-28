#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	char* str = (char*)malloc(sizeof(char)*101);
	scanf("%s",str);
	realloc(str,strlen(str)+1);
	int count=0;
	
	for(int i=0,pprev=-1,prev=-1; str[i]!='\0'; pprev=prev,prev=str[i++]){
		count++;
		if((pprev=='d' && prev=='z' && str[i]=='=')) count-=2;
		else if((prev=='c' && str[i]=='=') ||
			(prev=='c' && str[i]=='-') ||
			(prev=='d' && str[i]=='-') ||
			(prev=='l' && str[i]=='j') ||
			(prev=='n' && str[i]=='j') ||
			(prev=='s' && str[i]=='=') ||
			(prev=='z' && str[i]=='=') 
		) count--;
		
	}
	printf("%d",count);
	return 0;
}