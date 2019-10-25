 #!/usr/bin/python3
"""
forged by Kei Thoma
"""

class QuotientRingElement:
    def __init__(self, _mod, _value):
        self.mod_ = _mod
        self.value_ = _value % _mod

    def mod(self):
        return self.mod_

    def value(self):
        return self.value_

    def __pos__(self):
        return self

    def __neg__(self):
        return QuotientRingElement(self.mod_, - self.value_)

    def __str__(self):
        return "({} + {}Z)".format(self.value_, self.mod_)

    def __add__(self, _other):
        return QuotientRingElement(self.mod_, self.value_ + _other.value_)

    def __sub__(self, _other):
        return QuotientRingElement(self.mod_, self.value_ - _other.value_)

    def __mul__(self, _other):
        return QuotientRingElement(self.mod_, self.value_ * _other.value_)

    def __pow__(self, _other):
        return QuotientRingElement(self.mod_, self.value_ ** _other.value_)

class QuotientRing:
    def __init__(self, _mod):
        self.mod_ = _mod
        self.set_ = [self.construct_element(i) for i in range(0, _mod)]

    def mod(self):
        return self.mod_

    def set(self):
        return self.set_

    #def set_string(self):
    #    string = "["
    #    for element in self.set_:
    #        string.append("{}, "str(element))
    #    string.append("]")



    def construct_element(self, _value):
        return QuotientRingElement(self.mod_, _value)

    def find_zero_divisors(self):
        zero_divisors = []
        for left in self.set_:
            for right in self.set_:
                if (left * right).value() == 0 and left.value() != 0 and right.value() != 0:
                    zero_divisors.append(left)
        return zero_divisors



def main():
    print("BEGINN MODULE\n\n\n")

    mod = int(input("Input the 'n' for Z/nZ: "))
    test_obj  = QuotientRing(mod)
    print("The set of the ring is: {0}\n".format(test_obj.set))

    print("Now we want to add the last two elements together.")
    print("{0} + {1} = {2}".format(test_obj.set()[mod - 2], test_obj.set()[mod - 1], test_obj.set()[mod - 2] + test_obj.set()[mod - 1]))

    zero_divisors = test_obj.find_zero_divisors()
    for element in zero_divisors:
        print(element)

if __name__ == '__main__':
    main()
