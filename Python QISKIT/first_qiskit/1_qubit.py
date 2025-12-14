class Qubit:
    def __init__(self)
    self.alpha = 1.0
    self.beta = 0.0

    def Hadamard(self):
        new_alpha = (self.alpha + self.beta) / (2 ** 0.5)
        new_beta = (self.alpha - self.beta) / (2 ** 0.5)
        self.alpha = new_alpha
        self.beta = new_beta

    def measure(self):
        p0 = self.alpha ** 2

        r = (hash(str(self.alpha) + str(self.beta))%1000)/1000.0 
        if r < p0:
            self.alpha, self.beta = 1.0, 1.0
            return 0
            
        else:
            self.alpha, self.beta = 0.0, 1.0
            return 1
            
qubit = Qubit()
qubit.hadamard()

results = {0: 0, 1: 0}
for _ in range(1000):
    qubit = Qubit()
    qubit.Hadamard()
    result = qubit.measure()
    results[outcome] += 1

print(results)