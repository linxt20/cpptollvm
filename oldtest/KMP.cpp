int printf(char* a, ...);
int scanf(char* a, ...);

char stringone[100];
char stringanother[100];
int nextone[100];
int len;

int KMP()
{
	int i = 0, j = 0, flag = 0, pos;
	while(stringone[i] != 0)
	{
		if(j == -1 || stringone[i] == stringanother[j])
		{
			i = i + 1; 
			j = j + 1; 
			if(stringanother[j] == 0)
			{
				pos = i - len;
				printf("place: %d\n",pos);
				flag = 1;
			}
		}
		else j = nextone[j];
	}
	if(flag == 0)
		printf("false");
}
int main()
{
    int i,k;
	scanf("%s",stringone);
	scanf("%s",stringanother);

	len = 0;
	while(stringanother[len] != 0)
		len = len + 1;
    
	nextone[0] = -1;

	for(i = 1; i < len; i = i + 1)
	{
		k = nextone[i - 1];
		nextone[i] = 0;
		while(k >= 0)
		{
			if(stringanother[i - 1] == stringanother[k])
			{
				nextone[i] = k+1;
				break;
			}
			else
				k = nextone[k];
		}
	}

	KMP();
	return 0;
}