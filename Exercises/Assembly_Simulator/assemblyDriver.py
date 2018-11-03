from assemblySimulator import * 

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
