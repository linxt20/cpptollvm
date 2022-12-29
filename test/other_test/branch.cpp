int printf(char *s, ...);

int main(){
    int a = -1;
    if(1){
        printf("1\n");
    } else {
        printf("0\n");
    }
    int b = 1;
    if(a) {
        a = a + 1;
        printf("%d\n", a);
    } else {
        a = a - 1;
        printf("%d\n", a);
    }
    return 0;
}