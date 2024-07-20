# learn to produce results of a 4/3 bit adder input to numbers in binary output in decimal or binary ?

import numpy as np
from encephalon import NN


Data = list[tuple[list[int],int]]

def int_to_bin_list(i:int,n:int) -> list[int]:
    return list(map(int,list(bin(i)[2:].zfill(n))))

def n_bit_adder_data_generator(n: int) -> Data:
    D = [] 
    for i in range(2**n) :
        for j in range(2**n) :
            D.append(((int_to_bin_list(i,n) + int_to_bin_list(j,n)), i + j))
    return D


def data_spliter(D:Data,p:float)-> tuple[Data,Data]:
    T = D[:]
    np.random.shuffle(T)
    s = int(len(T) * p)
    return T[:s],T[s:]

def n_bit_adder_data(n:int, p:float) -> tuple[Data,Data]:
    return data_spliter(n_bit_adder_data_generator(n),p)

def ReLU(X):
    return np.maximum(0,X)

def softmax(X):
    return np.exp(X) / sum(np.exp(X))


    

training_data , test_data = n_bit_adder_data(2,0.5)

def foward_propagation(X,W,b,f):
    return f(W.dot(X) + b)

def main():
    Id = lambda x: x
    bill = NN([1,1])
    bill.load("/home/eleve/bill_2024-07-19T14:58:29.npz")
    X = np.array([0,1])
    print(bill.forward_propagation(X, g = Id))


if __name__ == "__main__":
    main()