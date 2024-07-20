import numpy as np
from encephalon import NN

data = np.array([[0,0], [0,1], [1,0], [1,1]])
labels = np.array([[0], [1], [1], [0]])


def main():
    xor = NN([2,3,1],name="xor")
    xor.train(data, labels, 100)


if __name__ == "__main__":
    main()