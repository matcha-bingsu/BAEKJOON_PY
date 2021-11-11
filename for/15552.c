#include <stdio.h>

int main(void)
{
    int num;
    int a;
    int b;
    int i;

    i = 0;
    scanf("%d",&num);
    while (i < num){
        scanf("%d %d", &a, &b);
        printf("%d\n",a+b);
        i++;
    }

}

