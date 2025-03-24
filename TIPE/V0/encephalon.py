#no g function it needs to be handled after or by error function or whatever
#or i could the function for each layer be controllable
# look into initialisation (He initialisation)
# compenser division par 10V des multiplieur dans le somateur
# dead neurons look into leaky ReLU L2 regularisation
# write handshakes
# momentum and other optimisations

# discrete parameters
# weights beween [-2.5, 2.5] potentialy larger for biases 
# use amp for bigger range ? 





import os
from dendron import *
from axon import *
import numpy as np
import json




class NN:
    def __init__(self,layers: list[int], serialInst: serial.Serial, name: str = "unnamed_model", f: activation_function_type = ReLU, g: activation_function_type = Id) -> None:

        self.lenght = len(layers) - 1
        if self.lenght <= 0 : raise Exception("not enough layers")

        self.serialInst = serialInst
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


    def set_weights_and_biases(self, timeout_delay = 1) -> None:
        parameters = {
            f"W:{key}": value.tolist() for key, value in self.W.items()
        }
        parameters.update({
            f"b:{key}": value.tolist() for key, value in self.b.items()
        })
        serial_write(self.serialInst, f"PARAMETERS {json.dumps(parameters)}\n")
        
        # Wait for acknowledgment
        handshake = serial_read(self.serialInst, timeout=timeout_delay).strip()
        if handshake != "ACK":
            raise Exception(f"Failed to set weights and biases: {handshake}")


    def use(self, X: np.ndarray, timeout_delay = 0.1) -> np.ndarray | None:
        X = np.array(X)  # Ensure X is a NumPy array
        serial_write(self.serialInst, f"INPUT {json.dumps(X.tolist())}\n")
        
        # Wait for acknowledgment
        handshake = serial_read(self.serialInst, timeout=timeout_delay).strip()
        if handshake != "ACK":
            print(f"Failed to process input: {handshake}")
            return None
        
        # Read the response
        response = serial_read(self.serialInst, timeout=timeout_delay).strip()
        if response:
            try:
                return json.loads(response.strip()) #convert to np array of right shape !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            except json.JSONDecodeError as e:
                print(f"Error decoding response: {response}, Error: {e}")
                return None
        print("No response received from serial.")
        return None
    
    def forward_propagation(self, X: np.ndarray) -> tuple[np.ndarray,list[np.ndarray]]:
        cache = []
        Y = np.array(X, ndmin=2)
        for i in range(1, self.lenght):
            C = np.dot(Y, self.W[i]) + self.b[i]
            cache.append((Y, C))
            Y = self.f(C)
        C = np.dot(Y, self.W[self.lenght]) + self.b[self.lenght]
        cache.append((Y,C))
        return self.use(X), cache
        # return self.g(C), cache

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
            np.dot(X.T, error, out=dW[n - i]) 
            np.copyto(db[n - i], error)
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
    

    def update(self,  dW: dict[int,np.ndarray], db: dict[int,np.ndarray], learning_rate: float = 0.01, timeout_delay=  1) -> None:
        for i in range(1,self.lenght + 1):
            self.W[i] -= learning_rate * dW[i]
            self.b[i] -= learning_rate * db[i]
        self.set_weights_and_biases(timeout_delay)

    def save(self, filename: str = "default"):
        if filename == "default" : filename = self.name
        np.savez(filename+ '_' + str(np.datetime64('now')), W = self.W, b = self.b)


    def load(self, filename: str):
        data = np.load(filename, allow_pickle=True)
        self.W = data['W'].item()
        self.b = data['b'].item()

    def train(self, 
          data: np.ndarray, 
          labels: np.ndarray, 
          epochs: int, 
          learning_rate: float = 0.01, 
          learning_rate_optimiser: learning_rate_optimizer_type = fixed_learning_rate(), 
          loss: error_function_type = mse, 
          batch_size: int = None, 
          saving: bool = False, 
          save_step: int = 1, 
          saving_improvement: float = 0.8, 
          err_min_init: float = 0.001, 
          printing: bool = True, 
          print_step: int = 10) -> None:
        """
        Train the neural network using gradient descent.

        Parameters:
        ----------
        data : np.ndarray
            Training data.
        labels : np.ndarray
            Training labels.
        epochs : int
            Number of epochs to train for.
        learning_rate : float, optional
            Initial learning rate, by default 0.01.
        learning_rate_optimiser : learning_rate_optimizer_type, optional
            Learning rate scheduler, by default fixed_learning_rate().
        loss : error_function_type, optional
            Loss function, by default mse.
        batch_size : int, optional
            Size of mini-batches. If None, full-batch training is used.
        saving : bool, optional
            Whether to save the model during training, by default False.
        save_step : int, optional
            Save the model every `save_step` epochs, by default 1.
        saving_improvement : float, optional
            Improvement factor for saving, by default 0.8.
        err_min_init : float, optional
            Initial minimum error for saving, by default 0.001.
        printing : bool, optional
            Whether to print training progress, by default True.
        print_step : int, optional
            Print progress every `print_step` epochs, by default 10.
        """
        
        samples = len(data)

        # Create directories for saving models
        if saving:
            err_min = err_min_init
            directory = self.name + "_training"
            os.makedirs(directory, exist_ok=True)
            start_time = str(np.datetime64('now'))
            subdirectory = os.path.join(directory, start_time)
            os.makedirs(subdirectory, exist_ok=True)

        # Training loop
        for epoch in range(epochs):

            err = 0

            # Shuffle data
            indices = np.arange(samples)
            np.random.shuffle(indices)
            data, labels = data[indices], labels[indices]

            # Mini-batch or full-batch processing
            batch_size = batch_size or samples
            for i in range(0, samples, batch_size):

                dW, db = self.empty_grad()

                x_batch = data[i:i + batch_size]
                y_batch = labels[i:i + batch_size]

                for j in range(batch_size):
                    # Forward pass
                    output, cache = self.forward_propagation(x_batch[j])

                    # Compute loss
                    err += loss[0](y_batch[j], output)

                    # Backward pass
                    dW, db = self.add_grad(dW, db, self.backward_propagation(output, y_batch[j], cache, backward_loss=loss[1]))

                # Normalize gradients
                dW, db = self.divide_grad(dW, db, batch_size)

                # Update weights and biases
                learning_rate = learning_rate_optimiser(learning_rate, epoch, dW, db)
                self.update(dW, db, learning_rate)

            # Average error
            err /= samples

            # Print progress
            if printing and (epoch + 1) % print_step == 0:
                print(f'Epoch {epoch + 1}/{epochs}   Error={err:.6f}')

            # Save model
            if saving and (epoch + 1) % save_step == 0:
                if err < err_min:
                    err_min = err * saving_improvement
                    self.save(os.path.join(subdirectory, f"{self.name}_{err:.6f}")) # scientific notation !!!!!!

        
def main():
    pass

if __name__ == "__main__":
    main()