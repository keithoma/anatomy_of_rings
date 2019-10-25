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
        self.set = [self.createQuotientRingElement(i) for i in range(0, _n)]

        
    def createQuotientRingElement(self, value):
        return QuotientRing.Element(self, value)

    class Element:
        def __init__(self, _QuotientRing, _value):
            self.QuotientRing = _QuotientRing
            self.n = _QuotientRing.n
            self.value = _value

        def __add__(self, _other):
            return QuotientRing.createQuotientRingElement((self + _other) % _n)




def main():
    print("BEGINN MODULE\n\n\n")

    n = int(input("Input the 'n' for Z/nZ: "))
    test_class = QuotientRing(n)
    print("The set of the ring is: {0}\n".format(test_class.set))

    print("Now we want to add the last two elements together.")
    print("{0} + {1} = {2}".format(test_class.set[n - 2], test_class.set[n-1], test_class.set[n - 2] + test_class.set[n - 1]))

if __name__ == '__main__':
    main()
