def main():
    # input
    N = int(input())
    # compute
    # output
    if (N//100) == 7 or (N//10 - (N//100)*10) == 7 or (N - (N//10)*10) == 7:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
