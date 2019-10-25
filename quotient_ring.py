#!/usr/bin/python3
"""
forged by Kei Thoma
"""

class QuotientRing:
    def __init__(self, _n):
        """
        Arguments:
        n (int)
            number of elements in the quotient ring, Z/nZ
        """
        if _n == 0:
            raise ValueError("Z/0Z is an empty set.")
        elif _n < 0:
            raise ValueError("n must be larger or equal to 1.")

        self.n = _n
        self.set = [QuotientRingElement(i) for i in range(0, _n)]

class QuotientRingElement:
    def __init__(self, _n, _value):
        self.n = _n
        self.value = _value

    def __add__(self, other):
        return (self + other) % _n




def main():
    print("BEGINN MODULE\n\n\n")

    n = int(input("Input the 'n' for Z/nZ: "))
    test_class = QuotientRing(n)
    print("The set of the ring is: {0}".format(test_class.set))

    print(test_class.set[n - 1] + test_class.set[n - 1])

if __name__ == '__main__':
    main()
