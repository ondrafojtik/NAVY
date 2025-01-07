import numpy as np
import matplotlib.pyplot as plt
import random

def Sigmoid(x):
    return (np.exp(x)) / (np.exp(x) + 1)

# derivative
def Sigmoid_(x):
    return (x * (1-x))


class XOR_Solver:
    def __init__(self):
        self.weights_H = np.random.uniform(size=(2,2))
        self.weights_O = np.random.uniform(size=(2,1))
        self.bias_H    = np.random.uniform(size=(1,2))
        self.bias_O    = np.random.uniform(size=(1,1))


    def train(self, data, expected_results, epochs):
        for i in range(0, epochs):
            self.train2(data, expected_results)

    def train2(self, data, expected):
        learning_rate = 1

        # guess
        out_H = Sigmoid(np.dot(data, self.weights_H)+self.bias_H)
        out_O = Sigmoid(np.dot(out_H, self.weights_O)+self.bias_O)

        # error
        sq_error = sum(0.5 * (expected - out_O)**2)
        #print(sq_error)
        # https://towardsdatascience.com/implementing-the-xor-gate-using-backpropagation-in-neural-networks-c1f255b4f20d
        error = expected - out_O

        # adjust w & b
        d_O = error * Sigmoid_(out_O)
        d_H = np.dot(d_O, self.weights_O.T) * Sigmoid_(out_H)

        self.weights_H += (np.dot(data.T, d_H)) * learning_rate
        self.weights_O += (np.dot(out_H.T, d_O)) * learning_rate

        self.bias_H += np.sum(d_H) * learning_rate
        self.bias_O += np.sum(d_O) * learning_rate


    def test(self, data):
        out_H = Sigmoid(np.dot(data, self.weights_H)+self.bias_H)
        out_O = Sigmoid(np.dot(out_H, self.weights_O)+self.bias_O)
        return out_O


train_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected = np.array([[0], [1], [1], [0]])


xor_s = XOR_Solver()

print("--------------------------------------")
print("Weight and bias before the learning phase:")
print(f"neuron_hidden1.weights \t {xor_s.weights_H[0]}")
print(f"neuron_hidden2.weights \t {xor_s.weights_H[1]}")
print(f"neuron_output.weights \t [{xor_s.weights_O[0].item()} {xor_s.weights_O[0].item()}]")
print(f"neuron_hidden1.bias \t {xor_s.bias_H[0][0]}")
print(f"neuron_hidden2.bias \t {xor_s.bias_H[0][1]}")
print(f"neuron_output.bias \t {xor_s.bias_O[0][0]}")

xor_s.train(train_data, expected, 10000)


test_data = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
test_expected = np.array([[0], [1], [1], [0]])

result = xor_s.test(test_data)

print("--------------------------------------")
print("Weight and bias after the learning phase:")
print(f"neuron_hidden1.weights \t {xor_s.weights_H[0]}")
print(f"neuron_hidden2.weights \t {xor_s.weights_H[1]}")
print(f"neuron_output.weights \t [{xor_s.weights_O[0].item()} {xor_s.weights_O[0].item()}]")
print(f"neuron_hidden1.bias \t {xor_s.bias_H[0][0]}")
print(f"neuron_hidden2.bias \t {xor_s.bias_H[0][1]}")
print(f"neuron_output.bias \t {xor_s.bias_O[0][0]}")

print("--------------------------------------")
print("Testing in progress..")
print("--------------------------------------")
print("Guess \t\t Expected output \t Is it equal?")

for i in range(0, len(result)):
    guess = result[i]
    expected = test_expected[i]
    isEqual = round(guess[0]) == expected

    print(f"{guess[0]:4f} \t {expected[0]} \t\t\t {isEqual[0]}")

print("--------------------------------------")
