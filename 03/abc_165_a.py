# ABC165A - We Love Golf

def main():
    # input
    K = int(input())
    A, B = map(int, input().split())

    # compute
    """WRITE BELOW"""
    C = 0
    # output
    for i in range(1, 1001):
        if A <= K*i <= B:
            print('OK')
            C = 1
            break
    if C == 0:
        print('NG')

if __name__ == '__main__':
    main()
