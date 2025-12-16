import math
import cmath

state = [
    1 + 0j,  # |00>
    0 + 0j,  # |01>
    0 + 0j,  # |10>
    0 + 0j   # |11>
]



def normalize(state):
    norm = math.sqrt(sum(abs(amplitude) ** 2 for amplitude in state))
    return [a/norm for a in state]

def print_state(state):
    basis = ['|00>', '|01>', '|10>', '|11>']
    for amp, b in zip(state, basis):
        if abs(amp) > 1e-6:
            print(f"{amp:.2f} {b}")
            print()

H = [
    [1/math.sqrt(2),  1/math.sqrt(2)],
    [1/math.sqrt(2), -1/math.sqrt(2)]
]

X = [
    [0, 1],
    [1, 0]
    ]

def apply_single_qubit_gate(state, gate, qubit):
    new_state = [0 + 0j] * 4
    
    for i in range(4):
        qubit_bit = (i >> (1 - qubit)) & 1
        for gate_bit in range(2):
            j = i ^ ((qubit_bit ^ gate_bit) << (1 - qubit))
            new_state[j] += gate[qubit_bit][gate_bit] * state[i]
    
    return new_state

def apply_cnot(state, control, target):
    new_state = state[:]

    for i in range(4):
        control_bit = (i >> (1 - control)) & 1
        if control_bit == 1:
            flipped = i ^ (1 << (1 - target))
            new_state[flipped] = state[i]
            new_state[i] = state[flipped]

            return new_state

print("Initial state:")
print_state(state)

# Apply Hadamard to qubit 0
state = apply_single_qubit_gate(state, H, qubit=0)
print("After H on qubit 0:")
print_state(state)

# Apply CNOT (0 -> 1)
state = apply_cnot(state, control=0, target=1)
print("After CNOT (0 -> 1):")
print_state(state)