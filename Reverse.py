x = input()
z = []
for i in range(int(x)):
    y = input()
    z.append(y)

z.reverse()
for i in range(int(x)):
    print(z[i])