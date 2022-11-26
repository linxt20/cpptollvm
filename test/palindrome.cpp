#include<cstdio>

int main(){
	int i = 0, j = 0;
	char m[100];
	scanf("%s", &m);
	while(m[i])
		i++;
	i--;
	while(j < i){
		if(m[j] != m[i]){
			printf("False");
			return 0;
		}
		i--;
		j++;
	}
	printf("True");
	return 0;
}
