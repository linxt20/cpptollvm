int printf(char* s, ...);

char test[100] = "hello, world!";

int main(){
    printf("%s", test);
    test[1] = test[0];
    printf("%s", test);
    return 0;
}