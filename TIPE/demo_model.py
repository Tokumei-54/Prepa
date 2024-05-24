# learn to produce results of a 4/3 bit adder input to numbers in binary output in decimal or binary ?
import numpy as np

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

training_data , test_data = n_bit_adder_data(2,0.5)
print("\n",training_data ,"\n\n", test_data)