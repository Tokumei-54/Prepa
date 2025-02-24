#no g function it needs to be handled after or by error function or whatever
#or i could the function for each layer be controllable
#function to send state W b to arduino
#foward prop though serial
#adaptable to any networtk send dimensions
# look into initialisation (He initialisation)
#compenser division par 10V des multiplieur dans le somateur
#comment faire des tension negatives en soustrayant 2,5 peut etre [0,5] -> [-2.5,2.5]
# dead neurons look into leaky ReLU L2 regularisation






import os
from dendron import *
from axon import *
import numpy as np
import json




class NN:
    def __init__(self,layers: list[int], serialInst: serial.Serial, name: str = "unnamed_model", f: activation_function_type = ReLU, g: activation_function_type = ReLU) -> None:

        if len(layers) <= 1 : raise Exception("not enough layers")

        self.serialInst = serialInst
        self.name = name

        self.f = f[0]
        self.backward_f = f[1]
        self.g = g[0]
        self.backward_g = g[1]


        self.W = {}
        self.b = {}

        for i in range(1, len(layers)):
            self.W[i] = np.random.randn(layers[i-1], layers[i]) * np.sqrt(2 / layers[i-1]) #He initialisation
            self.b[i] = np.zeros((1, layers[i]))


    def set_weights_and_biases(self) -> None:
        parts = []
        for key, value in self.W.items():
            parts.append(f"W:{key}={json.dumps(value.tolist())}")
        for key, value in self.b.items():
            parts.append(f"b:{key}={json.dumps(value.tolist())}")
        serial_write(self.serialInst, "PARAMETERS " + "; ".join(parts))


    def use(self, X: np.ndarray, timeout_delay = 0.1) -> np.ndarray | None: #test if timeout is enough
        response = serial_write_and_await(self.serialInst, f"INPUT {json.dumps(X)}", timeout=timeout_delay)         
        if response:
            try:
                return json.loads(response)
                # return np.ndarray(json.loads(response)) #possibly more parsing necessary
            except json.JSONDecodeError:
                print("Error decoding response")
                return None
        return None
