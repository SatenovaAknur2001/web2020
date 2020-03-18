a=[]
sum=0
j=0
n=int(input())
a=[int(s) for s in input().split()]
for i in range (len(a)//2):
    temp=a[i]
    a[i]=a[len(a)-i-1]
    a[len(a)-i-1]=temp
    for i in range (len(a)):
        print(a[i])