mainline = ["R", "N", "B", "Q", "K", "B", "N", "R"]
pawnline = ["P" for n in range(8)]
emptyline = ["__" for n in range(8)]

board = [
    [f"b{p}" for p in mainline],
    [f"b{p}" for p in pawnline],
    [c for c in emptyline],
    [c for c in emptyline],
    [c for c in emptyline],
    [c for c in emptyline],
    [f"w{p}" for p in pawnline],
    [f"w{p}" for p in mainline]
]
