x,y = input().split()
a = int(x)
b = int(y)
if ("0" not in x and "0" not in y and a != b):
    a = int(x[::-1])
    b = int(y[::-1])
if(a > b ):
    print(a)
else:
    print(b)
