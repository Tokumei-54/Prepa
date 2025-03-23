import threading
import numpy as np
import json
from dendron import *
import os

def run_sim(sim , port):
    thread = threading.Thread(target=sim, args=[port], daemon=True)
    thread.start()

def ANN(layers: list[int], f: activation_function_type = ReLU, g: activation_function_type = Id):
    def sim(port):
        I = np.zeros((1, layers[0]))
        W = {}
        b = {}
        for i in range(1, len(layers)):
            W[i] = np.random.randn(layers[i-1], layers[i]) * np.sqrt(2 / layers[i-1]) #He initialisation
            b[i] = np.zeros((1, layers[i]))
        
        def O(I,W,b,f,g):
            Y = I
            for i in range(1, len(W)):
                Y = f(np.dot(Y, W[i]) + b[i])[0]
            return g(np.dot(Y, W[len(W)]) + b[len(W)])[0]
        
        def process_command(command):
            if not command.strip():
                print("Empty command received.")
                return
            if command.startswith("SET"):
                parts = command.split()
                if len(parts) != 3:
                    os.write(port, b"Invalid SET command format.\n")
                param, voltage = parts[1], float(parts[2])
                
                if param.startswith("W"):
                    layer, row, col = map(int, param[1:].split(':'))
                    W[layer][row][col] = voltage
                elif param.startswith("b"):
                    layer, row = map(int, param[1:].split(':'))
                    b[layer][row] = voltage
                elif param.startswith("I"):
                    I[int(param[1:])] = voltage
                
                os.write(port, f"SET command executed: {param} set to {voltage}V\n".encode())
                # if channel != 255:
                #     os.write(port, f"SET command executed: {param} set to {voltage}V".encode())
                # else:
                #     os.write(port, b"Invalid parameter for SET command.")
            elif command.startswith("READ"):
                index = int(command.split()[1][1:])
                analog_value = O(I,W,b,f,g)[index]
                os.write(port, f"Analog value on O{index}: {analog_value}\n".encode())
            elif command.startswith("PARAMETERS"):
                command = command[11:]
                try:
                    doc = json.loads(command)
                    for key, values in doc.items():
                        if key.startswith("W"):
                            layer = int(key[2:])
                            W[layer] = np.array(values)
                        elif key.startswith("b"):
                            layer = int(key[1:])
                            b[layer] = np.array(values)
                    os.write(port, b"Weights and biases updated.\n")
                except json.JSONDecodeError as e:
                    print(f"Invalid PARAMETERS command: {command}, Error: {e}")
                    os.write(port, b"Invalid PARAMETERS command.\n")
            elif command.startswith("INPUT"):
                command = command[6:]
                values = json.loads(command)
                
                I = np.array(values)
                os.write(port, (json.dumps(O(I, W, b, f, g)) + "\n").encode())

        while True:
            command = b""
            while not command.endswith(b"\n"):
                command += os.read(port, 1)
            command = command.decode("utf-8").strip()
            process_command(command)
    return sim