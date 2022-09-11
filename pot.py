addends = int(input())
summ = 0
for i in range(addends):
    x = input()
    lastdig = x[-1]
    pow = int(x[:-1])**int(lastdig)
    summ += pow
print(summ)