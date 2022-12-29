int printf(char* s, ...);

int s[10];

int main() {
	int i, j;
	for(i = 1; i < 10; i++)
        for(j = 1; j < 10; j++)
		    printf("Hello, world!(%d, %d)\n", i, j);
    i = 0;
    while(i < 10){
        i = i + 1;
        printf("%d ", i);
    }
	return 0;
}