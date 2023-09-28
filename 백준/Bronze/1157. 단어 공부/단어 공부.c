#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
	char* str = (char*)calloc(1000001,sizeof(char));
	fgets(str,1000001,stdin);
	
	int count[26] = {0,};
	int i=0, max=0, maxindex=0;
	while(str[i]!='\0'){
		if(isalpha(str[i])){
			str[i] = toupper(str[i]);
			count[(str[i]-'A')] += 1;
			if(count[(str[i]-'A')] >= max){
				max = count[(str[i]-'A')];
				maxindex = str[i]-'A';
			}
		}
		i++;
	}
	
	
	for(int j=0; j<26; j++){
		if(count[j]==max && maxindex!=j) {
			printf("?"); return 0;
		}
	}
	printf("%c",maxindex+'A');
	return 0;
}