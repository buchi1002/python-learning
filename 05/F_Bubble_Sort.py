def bubble_sort(Xs: list) ->list:
    a = len(Xs)
    c = 1
    while c != 0:
        c = 0
        for i in range(a-1):
            if Xs[i] > Xs[i+1]:
                b = Xs[i]
                Xs[i] = Xs[i+1]
                Xs[i+1] = b
                c += 1
    return Xs
def main():
    # input
    As = list(map(int, input().split()))
    # compute
    print(bubble_sort(As))
    # output

if __name__ == '__main__':
    main()
