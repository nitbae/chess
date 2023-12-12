from process import SyntaxErr as SE
from process import Basics as BS
from board import board as brd

class mth:
    @classmethod
    def plc(cls, pos, key):
        exit("> SyntaxBreak -> Incorrect move") if SE.verify(pos, key="pos") else None
        return pos[0] if key == "col" else int(pos[1])
    
    @classmethod
    def fills(cls, wl, key, rev=False, sp=False): #wl -> way list; sp -. special conditions
        global brd
        missM = []
        missC = []
        for m in wl:
            match brd[8 - int(m[1])][ord(m[0]) - 65][0]:
                case "w" if key == "move":
                    wl[wl.index(m)] = "***"
                    missM.append(m)
                case "b" if key == "move" and sp == True:
                    wl[wl.index(m)] = "***"
                    missM.append(m)
                case "b" if key == "cap":
                    continue
                case _ if key == "cap":
                    wl[wl.index(m)] = "***"
                    missC.append(m)
        while "***" in wl:
            wl.remove("***")
        match rev:
            case False:
                return wl
            case True if key == "move":
                return missM
            case True if key == "cap":
                return missC

class Pawn:
    @classmethod
    def _way_(cls, pos):
        res = [f"{mth.plc(pos, key='col')}{mth.plc(pos, key='line') + 1}"]
        return res
    
    @classmethod
    def way(cls, pos):
        return mth.fills(Pawn._way_(pos), key='move', sp=True)

    @classmethod
    def _waycap_(cls, pos):
        res = [f"{chr(ord(mth.plc(pos, key='col')) + n)}{mth.plc(pos, key='line') + 1}" for n in [-1, 1]]
        res.extend(["H9", "O6"])
        n = 0
        for i in BS.edges(res):
            res.pop(i - n)
            n += 1
        return res
    
    @classmethod
    def waycap(cls, pos):
        return mth.fills(Pawn._waycap_(pos), key='cap')

class Rook:
    @classmethod
    def _way_(cls, pos):
        res = [f"{chr(n)}{mth.plc(pos, key='line')}" for n in range(65, 73)]
        sub = [f"{mth.plc(pos, key='col')}{n}" for n in range(1, 9)]

        sub.remove(pos)
        res.remove(pos)

        res.extend(sub)
        return res

    @classmethod
    def way(cls, pos):
        pass

    @classmethod
    def _waycap_(cls, pos):
        return Rook._way_(pos)

    @classmethod
    def waycap(cls, pos):
            pass
