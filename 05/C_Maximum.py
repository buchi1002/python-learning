def my_max(Xs: list) -> int:
    l = len(Xs)
    a = Xs[0]
    for i in range(l - 1):
        if a < Xs[i+1]:
            a = Xs[i+1]
    return a
def main():
    # input
    As = list(map(int, input().split()))
    # compute
    # output
    print(my_max(As))
if __name__ == '__main__':
    main()
