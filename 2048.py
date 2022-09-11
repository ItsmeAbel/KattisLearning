from shutil import move


A = [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]

A[0][1] = 4
for i in range(3):
    A[i][0],A[i][1],A[i][2],A[i][3] = input().split()

moveDir = int(input())
if (moveDir==0):
    for i in range(3):
        for k in range(2):
            if(A[i][3] + A[i][2] == A[i][3]):
                A[i][2] = A[i][3]
                A[i][2] = 0
            elif(A[i][3] == A[i][2]):
                A[i][2] = A[i][2] + A[i][3]
                A[i][3] = 0
            else:
                print("missing")
    
elif(moveDir == 1):
    sdfsd
elif moveDir == 2:
    sdfdsf
elif moveDir == 3:
    erdsf
else:
    print("You lost?")
print(A)