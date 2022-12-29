int printf(char *s, ...);

int main(){
    int a = 2531;
    int b = 46;
    int c = b + a;
    printf("%d\n", c);
    c = b - a;
    printf("%d\n", c);
    c = c + b * 50;
    printf("%d\n", c);
    double d = 1.23;
    printf("%lf\n", d);
    c = a / b;
    printf("%d\n", c);
    bool e = (d > 10);
    e = !e;
    bool f = (d < 0);
    f = f ^ e;
    return 0;
}