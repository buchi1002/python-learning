def main():
    # input
    S = input()
    T = input()
    Ts = list(T)
    # compute
    L = len(S)
    if S + Ts[L] == T:
        print("Yes")
    else:
        print("No")
    # output

if __name__ == '__main__':
    main()
