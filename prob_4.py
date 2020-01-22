import sys


def money_bin():
    tests = int(sys.stdin.readline())
    for _ in range(0, tests):
        gold, silver, bronze = [int(x) for x in sys.stdin.readline().split()]

        silver += (bronze - 1) // 5
        bronze = 5 if bronze % 5 == 0 else bronze % 5

        gold += (silver - 1) // 10
        silver = 10 if silver % 10 == 0 else silver % 10

        print(gold, silver, bronze)


money_bin()