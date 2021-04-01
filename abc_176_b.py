def main():
    # input
    N = list(input())
    L = len(N)
    # compute
    c = 0
    for i in range(L):
        c += int(N[i])
    if c%9 == 0:
        print("Yes")
    else:
        print("No")

    # output
if __name__ == '__main__':
    main()
