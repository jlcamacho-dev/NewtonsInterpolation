####################################################
# Author: Jose L. Camacho
# Class: CS 3010 - Numerical Methods
# Assignment 4 - Newton Polynomial Interpolation
####################################################

filename = 'datapoints.txt'


# ---------- start of file processing functions --------------- #
def preprocess(buff: list) -> list:
    nbuff = list()
    for i in range(len(buff)):
        if buff[i] != '':
            nbuff.append(buff[i])
    return nbuff


def clean(buff: list) -> list:
    nbuff = list()
    for i in range(len(buff)):
        if buff[i] != '':
            nbuff.append(buff[i])
    return nbuff


def strtofloat(buff: list) -> list:
    for i in range(len(buff)):
        buff[i] = float(buff[i])
    return buff


def filepro():
    x, y = [], []
    q = 0  # variable for file processing control

    # begin file proessing
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip('\n')
                line = line.split(' ')
                line = preprocess(line)
                line = clean(line)
                if q == 0:
                    x = strtofloat(line)
                    q += 1
                elif q == 1:
                    y = strtofloat(line)
                    q += 1
    except IOError:
        print('I/O error encountered')

    return x, y


# ---------- end of file processing functions --------------- #

# ---------- Beginning of Newtons Interpoloation ------------ #

def Coeff(xs: list, ys: list, cs: list):
    for i in range(len(ys)):
        cs.append(ys[i])

    n = len(cs)
    for j in range(1, n):
        for i in range(n-1, j, -1):
            cs[i] = (cs[i] - cs[i-1]) / (xs[i] - xs[i-j])
    return cs


def EvalNewton(xs: list, cs: list, z: float):
    n = len(xs)
    result = cs[-1]
    for i in range(n-1, 0, -1):
        result = result * (z - xs[i]) + cs[i]
    return result
# ---------- end of Newtons Interpoloation ------------------ #


def main() -> None:
    bVal = True
    while bVal:
        uInput = input('Value to evalute polynomial (q to quit): ')
        bVal = False if uInput == 'q' else True
        x, y = filepro()
        print(f'x is {x}')
        print(f'y is {y}')
        c = list()
        q = float(uInput) if uInput.isdigit() else None
        c = Coeff(x, y, c)
        r = EvalNewton(x, c, q)
        print(f'result = {r}')


if __name__ == '__main__':
    main()

