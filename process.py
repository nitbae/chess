class SyntaxErr:
    @classmethod
    def verify(cls, obj, key):
        pass

class Basics:
    rCol = [chr(n) for n in range(65, 73)]
    rLine = [str(n) for n in range(1, 9)]

    @classmethod
    def edges(cls, vect):
        res = []
        for elem in vect:
            if elem[0] in Basics.rCol and elem[1] in Basics.rLine:
                pass
            else:
                res.append(vect.index(elem))
        return res
