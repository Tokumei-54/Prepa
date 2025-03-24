import os
from typing import Callable
import numpy as np






activation_function_type = tuple[Callable[[np.ndarray], np.ndarray], Callable[[np.ndarray, np.ndarray], np.ndarray]]
error_function_type = tuple[Callable[[np.ndarray, np.ndarray], float], Callable[[np.ndarray, np.ndarray], np.ndarray]]
learning_rate_optimizer_type = Callable[[float,int,np.ndarray,np.ndarray],float]






ReLU: activation_function_type = (lambda x: np.maximum(0, x), lambda x,y: (x > 0)*y)


Id: activation_function_type = (lambda x: x, lambda x, y: y)


sigmoid: activation_function_type = (lambda x: 1 / (1 + np.exp(-x)), lambda x, y: (np.exp(-x) / (1 + np.exp(-x))**2)*y)


tanh: activation_function_type = (lambda x: np.tanh(x), lambda x, y: (1 - np.tanh(x)**2)*y)


def forward_softmax(x: np.ndarray) -> np.ndarray:
    tmp = np.exp(x)
    return tmp / np.sum(tmp)

def backward_softmax(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    tmp = np.exp(x)
    o = tmp / np.sum(tmp)
    n = np.size(o)
    return np.dot(y, (np.identity(n) - o.T) * o)

softmax: activation_function_type = (forward_softmax, backward_softmax)






mse: error_function_type = (lambda x , y: np.mean(np.power(y-x, 2)), lambda x, y: 2 * (x-y) / np.size(y))






def fixed_learning_rate() -> learning_rate_optimizer_type:
    return lambda learning_rate, epoch, dW, db : learning_rate


def time_based_decay(func: Callable[[int],float]) -> learning_rate_optimizer_type:
    return lambda learning_rate, epoch, dW, db : func(epoch)


def exponential_decay(k: int|float) -> learning_rate_optimizer_type:
    return time_based_decay(lambda x: np.exp(-k*x))


def step_decay(decay_rate: float = 0.5, step: int = 10) -> learning_rate_optimizer_type:
    return lambda learning_rate, epoch, dW, db : learning_rate * decay_rate if epoch % step == 0  else learning_rate






class NN:
    def __init__(self,layers: list[int], name: str = "unnamed_model", f: activation_function_type = ReLU, g: activation_function_type = ReLU) -> None:
        
        self.lenght = len(layers) - 1
        if self.lenght <= 0 : raise Exception("not enough layers")

        self.name = name

        self.f = f[0]
        self.backward_f = f[1]
        self.g = g[0]
        self.backward_g = g[1]


        self.W = {}
        self.b = {}

        for i in range(1, self.lenght + 1):
            self.W[i] = np.random.randn(layers[i-1], layers[i]) * np.sqrt(2 / layers[i-1]) #He initialisation
            self.b[i] = np.zeros((1, layers[i]))


    def use(self, X: np.ndarray) -> np.ndarray:
        Y = np.array(X, ndmin=2)
        for i in range(1, self.lenght):
            Y = self.f(np.dot(Y, self.W[i]) + self.b[i])
        return self.g(np.dot(Y, self.W[self.lenght]) + self.b[self.lenght])
    

    def forward_propagation(self, X: np.ndarray) -> tuple[np.ndarray,list[np.ndarray]]:
        cache = []
        Y = np.array(X, ndmin=2)
        for i in range(1, self.lenght):
            C = np.dot(Y, self.W[i]) + self.b[i]
            cache.append((Y, C))
            Y = self.f(C)
        C = np.dot(Y, self.W[self.lenght]) + self.b[self.lenght]
        cache.append((Y,C))
        return self.g(C), cache


    def backward_propagation(self, output: np.ndarray, label: np.ndarray, cache: list[np.ndarray], backward_loss: Callable[[np.ndarray, np.ndarray], np.ndarray] = mse[1]) -> tuple[dict[int,np.ndarray], dict[int,np.ndarray]]:
        dW, db = self.empty_grad()
        n = self.lenght
        X, C = cache.pop()
        error = self.backward_g(C, backward_loss(output,label))
        dW[n] = np.dot(X.T, error)
        db[n] = error
        error = np.dot(error, self.W[n].T)
        for i in range(1,n):
            X, C = cache.pop()
            error = self.backward_f(C, error)
            np.dot(X.T, error, out=dW[n - i])  # In-place operation for dW
            np.copyto(db[n - i], error)        # In-place copy for db
            error = np.dot(error, self.W[n-i].T)
        return dW, db
    

    def empty_grad(self) -> tuple[dict[int,np.ndarray], dict[int,np.ndarray]]:
        dW = {}
        db = {}
        for i in range(1, self.lenght + 1):
            dW[i] = np.zeros_like(self.W[i])
            db[i] = np.zeros_like(self.b[i])
        return dW, db
    

    def add_grad(self, dW: dict[int,np.ndarray], db: dict[int,np.ndarray], g:tuple[dict[int,np.ndarray], dict[int,np.ndarray]]) -> tuple[dict[int,np.ndarray], dict[int,np.ndarray]]:
        for i in range(1, self.lenght + 1):
            np.add(dW[i], g[0][i], out=dW[i])
            np.add(db[i], g[1][i], out=db[i])
        return dW, db


    def divide_grad(self, dW: dict[int,np.ndarray], db: dict[int,np.ndarray], n: int|float) -> tuple[dict[int,np.ndarray], dict[int,np.ndarray]]:
        for i in range(1,self.lenght + 1):
            np.divide(dW[i], n, out=dW[i])
            np.divide(db[i], n, out=db[i])
        return dW, db
    

    def update(self,  dW: dict[int,np.ndarray], db: dict[int,np.ndarray], learning_rate: float = 0.01) -> None:
        for i in range(1,self.lenght + 1):
            self.W[i] -= learning_rate * dW[i]
            self.b[i] -= learning_rate * db[i]


    def train(self, data: np.ndarray, labels: np.ndarray, epochs: int, learning_rate: float = 0.01, learning_rate_optimiser:learning_rate_optimizer_type = fixed_learning_rate(), loss: error_function_type = mse, saving: bool = False, save_step: int = 1, saving_improvement: float = 0.8, err_min_init: float = 0.001, printing: bool = True, print_step: int = 10) -> None:
        samples = len(data)
        if saving:
            err_min = err_min_init
            directory = self.name + "_training"
            if not os.path.exists(directory):
                os.makedirs(directory)
            start_time = str(np.datetime64('now'))
            subdirectory = os.path.join(directory,start_time)
            if not os.path.exists(subdirectory):
                os.makedirs(subdirectory)

        for i in range(epochs):
            err = 0
            dW, db = self.empty_grad()
            for j in range(samples):
                output, cache = self.forward_propagation(data[j])

                err += loss[0](labels[j], output)

                dW, db = self.add_grad(dW, db,self.backward_propagation(output, labels[j], cache, backward_loss=loss[1]))
            
            dW, db = self.divide_grad(dW, db, samples)
            learning_rate = learning_rate_optimiser(learning_rate, i, dW, db)
            self.update(dW, db, learning_rate)

            err /= samples
            if printing and (i+1)%print_step == 0 : 
                print('epoch %d/%d   error=%f' % (i+1, epochs, err))
            if saving and (i+1)%save_step == 0 : 
                if err < err_min :
                    err_min = err * saving_improvement
                    self.save(os.path.join(subdirectory, self.name + "_" + str(err)))
    

    def stochastic(self, data: np.ndarray, labels: np.ndarray, epochs: int, batch_size: int, learning_rate: float = 0.01, loss: error_function_type = mse) -> None:
        for epoch in range(epochs):
            indices = np.arange(data.shape[0])
            np.random.shuffle(indices)
            x_train, y_train = data[indices], labels[indices]
            
            for i in range(0, x_train.shape[0], batch_size):
                x_batch = x_train[i:i + batch_size]
                y_batch = y_train[i:i + batch_size]

                dW, db = self.empty_grad()
                for j in range(batch_size):
                    output, cache = self.forward_propagation(data[j])
                    dW, db = self.add_grad(dW, db,self.backward_propagation(output, labels[j], cache, backward_loss=loss[1]))
                
                dW, db = self.divide_grad(dW, db, batch_size)
                self.update(dW, db, learning_rate)
            
            print(epoch + 1,'/',epochs)

    
    def save(self, filename: str = "default"):
        if filename == "default" : filename = self.name
        np.savez(filename+ '_' + str(np.datetime64('now')), W = self.W, b = self.b)


    def load(self, filename: str):
        data = np.load(filename, allow_pickle=True)
        self.W = data['W'].item()
        self.b = data['b'].item()




def main():
    pass

if __name__ == "__main__":
    main()