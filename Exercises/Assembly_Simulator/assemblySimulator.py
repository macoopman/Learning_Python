class Assembly(object):
    def __init__(self):
        self.accumlator = 0
        self.memory = []
        self.memCounter = 0


    # Takes input and puts it in the accumulator
    def WRITE(self, value):
        self.accumlator = value

    # Returns contents of memory location 
    def READ(self, address):
        return self.memory[address-1]

    # Stores the Accumlator in a given memory address 
    def STORE(self, address):
        if address <= self.memCounter:
            self.memory[address] = self.accumlator
        else:
            self.memory.append(self.accumlator)
            self.memCounter += 1

    # Load the value at an address to the accumlator
    def LOAD(self, address):
        # Do some error checking
        self.accumlator = self.memory[address]

    # ADD value of address to value in accumluator -> stores in accumlator 
    def ADD(self, address):
        self.accumlator += self.memory[address]

    # SUB value of address to value in accumluator -> stores in accumlator 
    def SUB(self, address):
        self.accumlator -= self.memory[address]

    

    def __repr__(self):
        print(f"Accumulator = {self.accumlator}")
        print(f"\nMemory Size = {self.memCounter}")
        print("\nMemory:")
        for i in range(0, self.memCounter):
            print(f"Mem Loc {i} -> {self.memory[i]}") 



program = Assembly()
program.WRITE(1)
program.STORE(1)

program.WRITE(2)
program.STORE(2)

program.WRITE(88)
program.STORE(3)

program.LOAD(1)
program.ADD(0)
program.STORE(0)

program.WRITE(100)
program.STORE(4)

program.__repr__()
