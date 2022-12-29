int printf(char *s, ...);

int a;

int main(){
    a = 1;
    printf("%d\n", a);
    a = a * 4 + 1 ;
    printf("%d\n", a);
    return 0;
}