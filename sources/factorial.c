#include <stdio.h>

long factorial(long n)
{
    if (n<=1) {
        return 1;
    }
    return n*factorial(n-1);
}

int main(int argc, char **argv)
{
    printf("%ld\n", factorial(20));
    return 0;
}

