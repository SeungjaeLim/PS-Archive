n = int(input())
for i in range(n):
    if n%2 == 0:
        for j in range(n):
            if j%2 == 0:
                print("*", end='')
            else:
                print(" ", end='')
        print("")
        print(" ", end = '')
        for j in range(n):
            if j%2 == 0:
                print("*", end='')
            else:
                print(" ", end='')    
    else:
        for j in range(n):
            if j%2 == 0:
                print("*", end='')
            else:
                print(" ", end='')
        print("")
        print(" ", end = '')
        for j in range(n-2):
            if j%2 == 0:
                print("*", end='')
            else:
                print(" ", end='')  
    print("")
