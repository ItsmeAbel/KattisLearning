imp = input()
x = imp.split("-")
res = ""
for i in range(len(x)):
    k = x[i]
    j = k[0]
    res = res + j

print(res)