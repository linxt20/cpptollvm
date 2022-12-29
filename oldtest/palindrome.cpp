int printf(char* s, ...);
int scanf(char* s, ...);

int main(){
	int i = 0, j = 0;
	char m[100];
	scanf("%s", &m);
	while(m[i])
		i++;
	i--;
	while(j < i){
		if(m[j] != m[i]){
			printf("False\n");
			return 0;
		}
		i--;
		j++;
	}
	printf("True\n");
	return 0;
}