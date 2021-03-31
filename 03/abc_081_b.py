# ABC081B - Shift only

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    """WRITE BELOW"""
    C = 0
    D = 0
    while D == 0:
        for i in range(N):
            if As[i]%2 == 1:
                D = 1
                break
        if D == 0:
            As = list(map(lambda x: x>>1, As))
            C += 1
        else:
            break
    # output
    print(C)

if __name__ == '__main__':
    main()
