x = input()
a = 0
missedNums = []
if(1<= int(x) <= 100):
    for i in range(int(x)):
        y = input()
        if(1<=int(y)<=200):
            if not (int(y) == a+1):
                missedNums.append(a+1)
                b = 0
            else:
                b=1
            
        a = int(y)
        
if(b==1):
    print("good job")
else:
    for i in missedNums:
        print(i)