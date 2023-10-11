
#paildronme
a = input("enter a value")
sai_a=a[::-1]
if a == sai_a:
    print("paildromne is valid")
else:
    print("paildromne is not valid")

 #fibonacci series

def generate_fibonacci(n):
    fibonacci_series = []
    a,b = 0,1
    for _ in range(n):
         fibonacci_series.append(a)
         a,b = b, a + b
    return fibonacci_series

n = 10
fib_series = generate_fibonacci(n)
print(fib_series)



s1 = 0
s2 = 1
s = int(input())
i=1
if s==0:
    print(s1)
else:
    print(s1,s2,end=" ")
    while i<s-1:
        s3=s1+s2
        print(s3,end=" ")
        s1=s2
        s2=s3
        i=i+1

#fibonacci
a = 0
b = 1
c = 10
d = 1
while d<c-1:
    s = a+b
    print(s)
    a = b
    b = s
    d = d+1
