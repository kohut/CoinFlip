# Some fun coin flipping code
import numpy as np

def coinFlip():
    coin = np.random.rand(1)
    if coin < 0.5:
        return "H"
    else:
        return "T"

def countChange(n):
    change = 0
    last_flip = coinFlip()
    for i in range(1, n-1):
        new_flip = coinFlip()
        if new_flip != last_flip:
            change = change + 1
        last_flip = new_flip

    return change

def flipFraction(n):
    flipFrac = countChange(n) / n
    return flipFrac

print(flipFraction(10000))

