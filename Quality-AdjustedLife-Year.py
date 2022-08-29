x=input()
sum = 0
if(1<= int(x) <= 100):
    for i in range(int(x)):
        a,b = input().split()
        prod=float(a)*float(b)
        sum += prod
    print("%.3f" % sum)
