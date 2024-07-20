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
        Y = X
        for i in range(1, len(self.W)):
            Y = self.f(np.dot(Y, self.W[i]) + self.b[i])
        return self.g(np.dot(Y, self.W[len(self.W)]))
    
    def forward_propagation(self, X: np.ndarray) -> np.ndarray:
        Y = X
        for i in range(1, len(self.W)):
            C = np.dot(Y, self.W[i]) + self.b[i]
            self.cache.append((Y,C))
            Y = self.f(C)
        C = np.dot(Y, self.W[len(self.W)]) + self.b[len(self.W)]
        self.cache.append((Y,C))
        return self.g(C)

    def backward_propagation(self, output: np.ndarray, label: np.ndarray, deriv_loss = lambda x, y: 2*(x-y)/y.size) -> None:
        n = len(self.W)
        error = deriv_loss(output,label)
        X, C = self.cache.pop()
        self.dW[n] += np.dot(X.T, error)
        self.db[n] += error
        error = np.dot(self.deriv_g(C) * error, self.W[n].T)
        for i in range(1,n):
            X, C = self.cache.pop()
            self.dW[n - i] += np.dot(X.T, error)
            self.db[n - i] += error
            error = np.dot(self.deriv_f(C) * error, self.W[n].T)
    
    def reset_grad(self) -> None:
        for i in range(1, len(self.dW) + 1):
            self.dW[i] = np.zeros(self.dW[i].shape)
            self.db[i] = np.zeros(self.db[i].shape)
    
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
        for i in range(epochs):
            err = 0
            for j in range(samples):
                output = self.forward_propagation(data[j])

                err += loss[0](labels[j], output) # for display purpose only

                self.backward_propagation(output, labels[j], deriv_loss = loss[1])
            
            self.divide_grad(samples)
            self.update(learning_rate)

            err /= samples
            if i%10 == 0 : print('epoch %d/%d   error=%f' % (i+1, epochs, err))
    
    def save(self, filename = "default"):
        if filename == "default" : filename = self.name + '_' + str(np.datetime64('now'))
        np.savez(filename, W = self.W, b = self.b, dW = self.dW, db = self.db, cache = self.cache, f = self.f, g = self.g, deriv_f = self.deriv_f, deriv_g = self.deriv_g)

    def load(self, filename):
        data = np.load(filename, allow_pickle=True)
        self.W = data['W'].item()
        self.b = data['b'].item()
        self.dW = data['dW'].item()
        self.db = data['db'].item()
        self.cache = data['cache'].item()
        self.f = data['f'].item()
        self.deriv_f = data['deriv_f'].item()
        self.g = data['g'].item()
        self.deriv_g = data['deriv_g'].item()

    



ReLU = lambda x: np.maximum(0, x)
deriv_ReLU = lambda x: x > 0

Id = lambda x: x
deriv_Id = lambda x: 1

sigmoid = lambda x: 1 / (1 + np.exp(-x))
deriv_sigmoid = lambda x: np.exp(-x) / (1 + np.exp(-x))**2

softmax = lambda x: np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)

mse = lambda x , y: np.mean(np.power(y-x, 2))
deriv_mse = lambda x, y: 2*(x-y)/y.size

def main():
    bill = NN([2,2,2])
    bill.W[1] = np.array([[0, 1],[1, 0]])
    bill.W[2] = np.array([[1, 0],[0, 1]])
    X = np.array([0,1])
    print(bill.forward_propagation(X, g = Id))


if __name__ == "__main__":
    main()