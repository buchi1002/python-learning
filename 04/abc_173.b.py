def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]
    # compute
    Cs = [0, 0, 0, 0]
    for i in range(N):
        if Ss[i] == "AC":
            Cs[0] += 1
            continue
        if Ss[i] == "WA":
            Cs[1] += 1
            continue
        if Ss[i] == "TLE":
            Cs[2] += 1
            continue
        if Ss[i] == "RE":
            Cs[3] += 1
            continue
    # output
    print('AC x ',Cs[0])
    print('WA x ',Cs[1])
    print('TLE x ',Cs[2])
    print('RE x ',Cs[3])
if __name__ == '__main__':
    main()
