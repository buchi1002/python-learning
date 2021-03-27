
# ABC176A - Takoyaki

def main():
    # input
    N, X, T = map(int, input().split())

    # compute
    """WRITE BELOW"""
    if N%X == 0:
        print((N//X)*T)
    else:
        print((N//X + 1)*T)
    # output



if __name__ == '__main__':
    main()
