
# ABC159A - The Number of Even Pairs

def main():
    # input
    N, M = map(int, input().split())

    # compute
    """WRITE HERE"""

    # output
    print(int((N*(N - 1) + M*(M - 1))/2))


if __name__ == '__main__':
    main()
