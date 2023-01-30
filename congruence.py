"""
La congruence des nombres
a = b % n
b = a % n
n divise b - a
"""


def congruence():
    a = int(input("Entrez le premier nombre (a) : "))
    n = int(input("Entrez le nombre n : "))

    print(a % n)


if __name__ == '__main__':
    congruence()
