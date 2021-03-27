# ABC167B - Easy Linear Programming

def main():
    # input
    A, B, C, K = map(int, input().split())

    # compute
    """WRITE BELOW"""
    if K <= A:
        print(K)
    elif K <= A+B:
        print(A)
    else:
        print(2*A-K+B)

    # output


if __name__ == '__main__':
    main()
