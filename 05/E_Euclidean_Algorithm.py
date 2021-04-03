def gcd(Xs: list) -> int:
    x = Xs[0]
    y = Xs[1]
    while y != 0 or y != 1:
        b = x%y
        x = y
        y = b
        if b == 0:
            break
    if y == 0:
        return x
    else:
        return y

def main():
    # input
    Ns = list(map(int, input().split()))
    # compute
    # output
    print(gcd(Ns))
if __name__ == '__main__':
    main()
