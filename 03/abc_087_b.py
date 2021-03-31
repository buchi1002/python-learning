# ABC087B - Coins

def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    # compute
    """WRITE BELOW"""
    COUNT = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                J = a*500 + b*100 + c*50
                if J == X:
                    COUNT += 1
    # output
    print(COUNT)

if __name__ == '__main__':
    main()
