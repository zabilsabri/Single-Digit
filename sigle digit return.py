_foundby_ = "zabilsabri"

n = "55"
x = list(map(int, n))

while len(x) != 1:
    x = x[0] + x[1]
    x = str(x)
    x = list(map(int, x))
    if len(x) == 1:
        print(x)