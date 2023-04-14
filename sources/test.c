int zero(void)
{
    return 0;
}

int inc(int x)
{
    return x+1;
}

int add(int x, int y)
{
    return x+y;
}

int foo(int x)
{
    int r = 0;
    while (x--) {
        r++;
    }
    return r;
}

int main(void)
{
    int a = zero();
    int b = inc(a);
    int c = add(a, b);
    int d = foo(c);
    return c;
}
