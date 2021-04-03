def fibonacci(x: int) -> int:
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
def main():
    # input
    N = int(input())
    # compute

    # output
    print(fibonacci(N))
if __name__ == '__main__':
    main()
