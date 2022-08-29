R1,S = input().split()
if (-1000 <= int(R1) <= 1000 and -1000 <= int(S) <= 1000):
    x = (int(S)*2) - int(R1)
    print(x)
else:
    print('Error')

