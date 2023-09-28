#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	char* str = (char*)calloc(101,sizeof(char));
	gets(str);
	//fgets(str,101,stdin); 
	int last = strlen(str)-1;
	int first = 0;
	while(str[first++]==str[last--]) 
		if(first>=last){
			printf("1");
			return 0;
		}
	printf("0");
	return 0;
}