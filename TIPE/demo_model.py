# learn to produce results of a 4/3 bit adder input to numbers in binary output in decimal or binary ?

Input = list[tuple[list[int],int]]

def int_to_bin_list(i:int,n:int) -> list[int]:
    return list(map(int,list(bin(i)[2:].zfill(n))))

def n_bit_adder_data_generator(n: int) -> Input:
    T = [] 
    for i in range(2**n - 1) :
        for j in range(2**n - 1) :
            T.append(((int_to_bin_list(i,n) + int_to_bin_list(j,n)), i + j))
    return T

print(n_bit_adder_data_generator(2))