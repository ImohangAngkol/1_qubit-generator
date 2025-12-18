import math
import random


# Linear Algebra

def matrix_vector_mul(matrix, vector):
    result = []
    for row in matrix:
        value = 0
        for i in range(len(vector)):
            value += row[i] * vector[i]
        result.append(value)
    return result


def normalize(state):
    norm = math.sqrt(sum(abs(a)**2 for a in state))
    return [a / norm for a in state]



# Qubit States

def zero_state():
    return [1, 0] 

def one_state():
    return [0, 1]  



# Quantum Gates

HADAMARD = [
    [1 / math.sqrt(2),  1 / math.sqrt(2)],
    [1 / math.sqrt(2), -1 / math.sqrt(2)]
]

PAULI_X = [
    [0, 1],
    [1, 0]
]

CNOT = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
]


# Apply Quantum Gates

def apply_gate(state, gate):
    return normalize(matrix_vector_mul(gate, state))


def tensor_product(a, b):
    result = []
    for i in a:
        for j in b:
            result.append(i * j)
    return result



# Measurement

def measure(state):
    probabilities = [abs(a)**2 for a in state]
    r = random.random()
    cumulative = 0

    for i, p in enumerate(probabilities):
        cumulative += p
        if r < cumulative:
            return i



# Superposition

print("Single Qubit Superposition:")
qubit = zero_state()
qubit = apply_gate(qubit, HADAMARD)
print("State:", qubit)
print("Measurement:", measure(qubit))



# Demo: Entanglement

print("\nTwo-Qubit Entanglement:")
q0 = zero_state()
q1 = zero_state()

# |00⟩
two_qubit = tensor_product(q0, q1)

# H on first qubit
two_qubit = [
    two_qubit[0] / math.sqrt(2),
    two_qubit[1] / math.sqrt(2),
    two_qubit[2] / math.sqrt(2),
    two_qubit[3] / math.sqrt(2)
]

# Apply CNOT
two_qubit = normalize(matrix_vector_mul(CNOT, two_qubit))

print("Entangled State:", two_qubit)
print("Measurement:", measure(two_qubit))

#jiandale I know gabasa ka ani right now HAHHAHAHAHBHA