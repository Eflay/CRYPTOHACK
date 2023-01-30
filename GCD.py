#!/usr/bin/python3

"""
Greatest Common Divisor et Bezout Identity
"""

# https://www.youtube.com/watch?v=BkK1_FspgYQ


def bezout():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    L1 = [a, 1, 0]
    L2 = [b, 0, 1]

    while L2[0] > 0:
        L = L2[:]
        q = L1[0] // L2[0]

        for i in range(0, 3):
            L2[i] = L1[i] - q * L2[i]
        L1 = L
    print(f"Le GCD est de {L1[0]}, le u est de {L1[1]} et le v de {L1[2]}")


if __name__ == '__main__':
    bezout()