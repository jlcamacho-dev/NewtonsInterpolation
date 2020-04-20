####################################################
# Author: Jose L. Camacho
# Class: CS 3010 - Numerical Methods
# Assignment 4 - Newton Polynomial Interpolation
# Description - this program takes in a positive
# number n in which it will generate n data points
####################################################
import random
import datetime
from timeit import default_timer as timer

filename = 'test.txt'


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


def dataPro(n: int):
    x, y = [], []
    dupes = {}

    # generate y values
    for i in range(n):
        y.append(random.randint(-5000, 5000))

    # generate x values (can not repeat)
    for i in range(n):
        bVal = True
        while bVal:
            tVal = random.randint(-5000, 5000)
            if tVal not in dupes:
                x.append(tVal)
                dupes[tVal] = 1
                bVal = False

    # write data points to file
    currentDT = datetime.datetime.now()  # get timestamp
    filename = f'datapoints_{currentDT.hour}_{currentDT.minute}_{currentDT.second}.txt'

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(x))
            f.write('\n')
            f.write(str(y))
            f.write('\n')
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
        start = timer()
        uInput = input('Please enter number of data points (q to quit): ')
        bVal = False if uInput == 'q' else True
        n = int(uInput) if uInput.isdigit() else None
        x, y = dataPro(n)
        c = list()
        c = Coeff(x, y, c)
        result = EvalNewton(x, c, random.randint(-1000, 1000))
        end = timer()
        print(f'result = {result} at {end - start}s')


if __name__ == '__main__':
    main()