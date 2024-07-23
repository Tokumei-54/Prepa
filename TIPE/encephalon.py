import os
import numpy as np


class NN:
    def __init__(self,layers: list[int], name = "model", f = (lambda x: np.maximum(0, x),  lambda x: x > 0), g = (lambda x: x, lambda x: 1)) -> None:

        if len(layers) <= 1 : raise Exception("not enough layers")

        self.name = name

        self.f = f[0]
        self.deriv_f = f[1]
        self.g = g[0]
        self.deriv_g = g[1]


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

    def backward_propagation(self, output: np.ndarray, label: np.ndarray, deriv_loss = lambda x, y: 2*(x-y)/y.size) -> None:
        n = len(self.W)
        X, C = self.cache.pop()
        error = self.deriv_g(C) * deriv_loss(output,label)
        self.dW[n] += np.dot(X.T, error)
        self.db[n] += error
        error = np.dot(error, self.W[n].T)
        for i in range(1,n):
            X, C = self.cache.pop()
            error = self.deriv_f(C) * error
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

    def train(self, data, labels, epochs, learning_rate = 0.01, loss = (lambda x , y: np.mean(np.power(y-x, 2)),  lambda x, y: 2*(x-y)/y.size)) -> None:
        samples = len(data)
        self.reset_grad()
        self.cache = []

        err_min = 0.001
        directory = self.name + "_training"
        if not os.path.exists(directory):
            os.makedirs(directory)

        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = self.forward_propagation(data[j])

                err += loss[0](labels[j], output) # for display purpose only

                self.backward_propagation(output, labels[j], deriv_loss = loss[1])
            
            self.divide_grad(samples)
            self.update(learning_rate)

            err /= samples
            if (i+1)%100 == 0 : 
                print('epoch %d/%d   error=%f' % (i+1, epochs, err))
                if err < err_min :
                    err_min = err *0.8
                    self.save(os.path.join(directory, self.name + "_" + str(err)))

    
    def save(self, filename = "default"):
        if filename == "default" : filename = self.name
        np.savez(filename+ '_' + str(np.datetime64('now')), W = self.W, b = self.b)

    def load(self, filename):
        data = np.load(filename, allow_pickle=True)
        self.W = data['W'].item()
        self.b = data['b'].item()

    



ReLU = (lambda x: np.maximum(0, x), lambda x: x > 0)

Id = (lambda x: x, lambda x: 1)

sigmoid = (lambda x: 1 / (1 + np.exp(-x)), lambda x: np.exp(-x) / (1 + np.exp(-x))**2)

tanh = (lambda x: np.tanh(x), lambda x: 1 - np.tanh(x)**2)

softmax = lambda x: np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

mse = (lambda x , y: np.mean(np.power(y-x, 2)), lambda x, y: 2*(x-y)/y.size)

def main():
    pass


if __name__ == "__main__":
    main()