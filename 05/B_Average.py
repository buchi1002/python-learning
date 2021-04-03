def average(Ys: list) -> float:
    a = 0
    for i in range(len(Ys)):
        a += Ys[i]
    a = a/len(Ys)
    return a
def main():
    # input
    As = list(map(int, input().split()))
    # compute
    # output
    print('{:.1f}'.format(average(As)))
if __name__ == '__main__':
    main()
