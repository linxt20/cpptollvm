int KMP(char* pattern, char* text){
    int n, m, k, q, i;
    int pai[30];
    pai[0] = -1;
    k = -1;
    n = strlen(text);
    m = strlen(pattern);
    for(q = 1; q < m; q++){
        while(k > -1 && pattern[k + 1] != pattern[q])
            k = pai[k];
        if(pattern[k + 1] == pattern[q])
            k++;
        pai[q] = k;
    }
    q = -1;
    for(i = 0; i < n; i++){
        while(q > -1 && pattern[q + 1] != text[i])
            q = pai[q];
        if(pattern[q + 1] == text[i])
            q++;
        if(i < m - 1)
            continue;
        if(q + 1 == m)
            return i - m + 1;
    }
    return -1;
}

int main(){
	int KMP_result;
	char text[30] = "qwertyuiopasdfghjklzxcvbnm";
	char pattern[5] = "ghjk";
	KMP_result = KMP(pattern, text);
	printf("%d", KMP_result);
	return 0;
}

