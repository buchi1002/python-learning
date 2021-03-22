# ABC183B - Billiards

def main():
    # input
    SX, SY, GX, GY = map(int, input().split())

    # compute
    x = (SY)*(GX - SX)/(GY + SY) + SX
    # output
    print(x)


if __name__ == '__main__':
    main()
