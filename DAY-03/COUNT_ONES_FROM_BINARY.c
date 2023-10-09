#include<stdio.h>
main()
{
  int a,c=0
  scanf("%d",&a);
  while(a)
  {
    c++;
    a=a&(a-1);
  }
  printf("%d",c);
}
