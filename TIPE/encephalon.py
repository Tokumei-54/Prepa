import os
import numpy as np


ReLU = (lambda x: np.maximum(0, x), lambda x,y: (x > 0)*y)

Id = (lambda x: x, lambda x, y: y)

sigmoid = (lambda x: 1 / (1 + np.exp(-x)), lambda x, y: (np.exp(-x) / (1 + np.exp(-x))**2)*y)

tanh = (lambda x: np.tanh(x), lambda x, y: (1 - np.tanh(x)**2)*y)

def forward_softmax(x):
    tmp = np.exp(x)
    return tmp / np.sum(tmp)

def backward_softmax(x, y):
    tmp = np.exp(x)
    o = tmp / np.sum(tmp)
    n = np.size(o)
    return np.dot(y, (np.identity(n) - o.T) * o)

softmax = (forward_softmax, backward_softmax)


mse = (lambda x , y: np.mean(np.power(y-x, 2)), lambda x, y: 2 * (x-y) / np.size(y))


class NN:
    def __init__(self,layers: list[int], name = "model", f = ReLU, g = ReLU) -> None:

        if len(layers) <= 1 : raise Exception("not enough layers")

        self.name = name

        self.f = f[0]
        self.backward_f = f[1]
        self.g = g[0]
        self.backward_g = g[1]


        self.W = {}
        self.b = {}
        self.dW = {}
        self.db = {}
        self.cache = []

        for i in range(1, len(layers)):
            self.W[i] = np.random.randn(layers[i-1], layers[i]) * np.sqrt(2 / layers[i-1])
            self.b[i] = np.zeros((1, layers[i]))
            self.dW[i] = np.zeros((layers[i-1], layers[i]))
            self.db[i] = np.zeros((1, layers[i]))
        
    def use(self, X: np.ndarray) -> np.ndarray:
        Y = np.array(X, ndmin=2)
        for i in range(1, len(self.W)):
            Y = self.f(np.dot(Y, self.W[i]) + self.b[i])
        return self.g(np.dot(Y, self.W[len(self.W)]))
    
    def forward_propagation(self, X: np.ndarray) -> np.ndarray:
        Y = np.array(X, ndmin=2)
        for i in range(1, len(self.W)):
            C = np.dot(Y, self.W[i]) + self.b[i]
            self.cache.append((Y,C))
            Y = self.f(C)
        C = np.dot(Y, self.W[len(self.W)]) + self.b[len(self.W)]
        self.cache.append((Y,C))
        return self.g(C)

    def backward_propagation(self, output: np.ndarray, label: np.ndarray, backward_loss = mse[1]) -> None:
        n = len(self.W)
        X, C = self.cache.pop()
        error = self.backward_g(C, backward_loss(output,label))
        self.dW[n] += np.dot(X.T, error)
        self.db[n] += error
        error = np.dot(error, self.W[n].T)
        for i in range(1,n):
            X, C = self.cache.pop()
            error = self.backward_f(C, error)
            self.dW[n - i] += np.dot(X.T, error)
            self.db[n - i] += error
            error = np.dot(error, self.W[n-i].T)
    
    def reset_grad(self) -> None:
        for i in range(1, len(self.W) + 1):
            self.dW[i] = np.zeros(self.W[i].shape)
            self.db[i] = np.zeros(self.b[i].shape)
    
    def divide_grad(self,n) -> None:
        for i in range(1, len(self.dW) + 1):
            self.dW[i] /= n
            self.db[i] /= n
    
    def update(self, learning_rate = 0.01):
        for i in range(1,len(self.W) + 1):
            self.W[i] -= learning_rate * self.dW[i]
            self.b[i] -= learning_rate * self.db[i]

    def train(self, data, labels, epochs, learning_rate = 0.01, loss = mse, err_min_init = 0.001, print_step=100) -> None:
        samples = len(data)
        self.reset_grad()
        self.cache = []

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
            for j in range(samples):
                output = self.forward_propagation(data[j])

                err += loss[0](labels[j], output) # for display purpose only

                self.backward_propagation(output, labels[j], backward_loss=loss[1])
            
            self.divide_grad(samples)
            self.update(learning_rate)

            err /= samples
            if (i+1)%print_step == 0 : 
                print('epoch %d/%d   error=%f' % (i+1, epochs, err))
                if err < err_min :
                    err_min = err *0.8
                    self.save(os.path.join(subdirectory, self.name + "_" + str(err)))

    
    def save(self, filename = "default"):
        if filename == "default" : filename = self.name
        np.savez(filename+ '_' + str(np.datetime64('now')), W = self.W, b = self.b)

    def load(self, filename):
        data = np.load(filename, allow_pickle=True)
        self.W = data['W'].item()
        self.b = data['b'].item()


def main():
    pass


if __name__ == "__main__":
    main()