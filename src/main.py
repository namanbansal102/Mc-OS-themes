from functools import reduce
N=input().split()
Nint= [int(j) for j in N]
M=input().split()
Mint= [int(j) for j in M]
Nint=set(Nint)
Mint=set(Mint)
res=Nint.symmetric_difference(Mint)
res=list(res)
for k in sorted(res):
    print(k, end=' ')
sum1=0
for item in res:
    sum1+=item
print(sum1)
