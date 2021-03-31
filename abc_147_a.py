# ABC147A - Blackjack

def main():
    # input
    As = list(map(int, input().split()))
    # compute
    """WRITE BELOW"""
    A = 0
    for i in range(3):
        A += As[i]
    # output
    if A >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()
