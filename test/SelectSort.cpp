int printf(char* s, ...);
int scanf(char* s, ...);

int main(){
	int i, j, n, min, index, temp;
	int m[100];
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%d", m[i]);
	}
	for(i = 0; i < n; i++){
		min = m[i];
		index = i;
		for(j = i + 1; j < n; j++){
			if(min > m[j]){
				min = m[j];
				index = j;
			}
		}
		temp = m[index];
		m[index] = m[i];
		m[i] = temp;
	}
	for(i = 0; i < n; i++)
		printf("%d", m[i]);
	printf("\n");
	return 0;
}
