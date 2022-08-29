x,y,n = input().split()
i = 1
if(1<= int(x) < int(y)<= int(n)<= 100):
    for i in range(int(n)):
        i += 1
        if(i % int(x) == 0 and i % int(y) == 0):
            print('FizzBuzz')
        elif(i % int(y) == 0):
            print('Buzz')
        elif(i % int(x) == 0):
            print('Fizz')
        else:
            print(i)
