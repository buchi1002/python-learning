def main():
    # input
    A, B, C = list(map(int, input().split()))
    # compute
    #Aが最大になるよう入れ替え
    if A < B :
        D = A
        A = B
        B = D
    if A < C :
        D = A
        A = C
        C = D




    # output
    print(10*A+B+C)
if __name__ == '__main__':
    main()
