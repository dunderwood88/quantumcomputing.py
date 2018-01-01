from qubit_manipulators import *
from qubit_register import *

q = QubitRegister(3)
hadamard_gate(q)

print(q.measure_register_str())
