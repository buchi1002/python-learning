# ABC168A - ∴ (Therefore)

def main():
    # input
    N = int(input())

    # compute
    """WRITE BELOW"""
    N = N % 10
    if N == 3:
        print("bon")
    elif N == 0 or N == 1 or N == 6 or N == 8:
        print("pon")
    else:
        print("hon")
    # output


if __name__ == '__main__':
    main()
