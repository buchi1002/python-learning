def gcd(x: int, y: int) -> int:
    if y > x:
        a = x
        x = y
        y = a
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
    N, M = map(int, input().split())
    # compute
    # output
    print(gcd(N, M))
if __name__ == '__main__':
    main()
