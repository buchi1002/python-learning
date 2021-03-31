# ABC137A - +-x

def main():
    # input
    A, B = map(int, input().split())

    # compute
    """WRITE BELOW"""
    if B >= 0:#Bが正なら-Bより+Bが大きい
        Y = A + B
    else:
        Y = A - B
    X = A*B
    if X < Y:
        X = Y
    # output
    print(X)

if __name__ == '__main__':
    main()
