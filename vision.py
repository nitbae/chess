from process import SyntaxErr as SE
from process import Basics as BS
from board import board, call

class mth:
    @classmethod
    def plc(cls, pos, key):
        #exit("> SyntaxBreak -> Incorrect move") if SE.verify(pos, key="pos") else None
        return pos[0] if key == "col" else int(pos[1])
    
    @classmethod
    def blocks(cls, pos, waylist, key): #key -> 'move', 'capt'
        global board
        res = []
        U, D, R, L = mth.separate(pos, waylist, [k for k in ["U", "D", "R", "L"]])
        try:
            U.reverse() if int(U[0][1]) > int(U[-1][1]) else None
        except:
            pass

        try:
            R.reverse() if ord(R[0][0]) > ord(R[-1][0]) else None
        except:
            pass

        try:
            D.reverse() if int(D[0][1]) < int(D[-1][1]) else None
        except:
            pass

        try:
            L.reverse() if ord(L[0][0]) < ord(L[-1][0]) else None
        except:
            pass
        print(U, D, R, L)

        for tr in U, D, R, L: #tr -- transition
            flag = True
            for m in tr:
                match board[8 - int(m[1])][ord(m[0]) - 65][0]:
                    case "w":
                        if tr.index(m) == 0:
                            pass
                        else:
                            res.extend(tr[:tr.index(m)]) if key == "move" else None
                        flag = False
                        break
                    case "b":
                        if tr.index(m) == 0:
                            res.extend([tr[0]]) if key == "capt" else None
                        else:
                            res.extend(tr[:tr.index(m)]) if key == "move" else res.append(m)
                        flag = False
                        break
            res.extend(tr) if flag and key == "move" else None
            print(res)
        return list(set(res))
                
    @classmethod
    def separate(cls, pos, waylist, side): #side -> 'U', 'D', 'R', 'L'
        U = []
        D = []
        R = []
        L = []
        p0 = mth.plc(pos, key='col')
        p1 = str(mth.plc(pos, key='line'))

        acco = {
            "U": U,
            "D": D,
            "R": R,
            "L": L
        }

        for m in waylist:
            match m[0]:
                case p0 if m[1] > p1:
                    U.append(m)
                case p0 if m[1] < p1:
                    D.append(m)
                case _:
                    p0 = mth.plc(pos, key='col')
                    if ord(m[0]) > ord(p0):
                        R.append(m)
                    else:
                        L.append(m)
        return [acco.get(k) for k in side]

class Pawn:
    @classmethod
    def _way_(cls, pos):
        return [f"{mth.plc(pos, key='col')}{mth.plc(pos, key='line') + 1}"]
    
    @classmethod
    def way(cls, pos):
        return mth.blocks(pos, Pawn._way_(pos), key='move')

    @classmethod
    def _waycap_(cls, pos):
        res = [f"{chr(ord(mth.plc(pos, key='col')) + n)}{mth.plc(pos, key='line') + 1}" for n in [-1, 1]]
        n = 0
        for i in BS.edges(res):
            res.pop(i - n)
            n += 1
        return res
    
    @classmethod
    def waycap(cls, pos):
        return mth.blocks(pos, Pawn._waycap_(pos), key='capt')

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
        return mth.blocks(pos, Rook._way_(pos), key='move')

    @classmethod
    def _waycap_(cls, pos):
        return Rook._way_(pos)

    @classmethod
    def waycap(cls, pos):
        return mth.blocks(pos, Rook._waycap_(pos), key='capt')

call(board)
