int printf(char* s, ...);

char test[100] = "hello, world!";

int main(){
    printf("%s\n", test);
    test[1] = test[0];
    printf("%s\n", test);
    return 0;
}