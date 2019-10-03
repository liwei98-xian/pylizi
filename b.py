a='*'
n=int(input('请输入一个数字：'))
for i in range(1,n,2):
    print((i*'*').center(n-1))
for i in reversed(range(1,n-2,2)):
    print((i*a).center(n-1))
