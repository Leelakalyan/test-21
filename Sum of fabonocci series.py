a=-1
b=1
sum=0
n=int(input('enter n value:'))
for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c
    sum=sum+c
print('sim is:',sum)

Output:
enter n value:
10
0
1
1
2
3
5
8
13
21
34
sim is: 88
