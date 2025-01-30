

def print_pattern(N):
    for i in range(1, N + 1):
        for j in range(i):
            print('*', end=' ')
        print()
N=int(input("entre the number"))
print_pattern(N)
