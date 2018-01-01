from qubit_manipulators import *
from math import *


def grover_search(qubits, oracle_function):
    """
    Grover search algorithm for querying a quantum oracle which promises a single
    solution.
    This algorithm finds a solution using O(sqrt(N)) queries to the oracle, whereas
    classically it would take O(N) queries.

    :param qubits: the qubit register, consisting of n-1 input qubits, and 1 ancillary qubit
    :param oracle_function: the oracle function which recognises the solution. Has a
    search space of N = 2^n, where n = number of qubits
    """

    # 1) flip bottom qubit
    pauli_x_gate(qubits, 1)

    # 2) hadamard all qubits
    hadamard_gate(qubits)

    # 3) apply the oracle function
    qubits.manipulate(oracle_function)

    # 4) grover diffusion operation
    for it in range(1, int(floor(sqrt(pow(2, qubits.size())) * (pi/4)))):

        # i) hadamard top qubits
        for q in range(qubits.size(), 1, -1):
            hadamard_gate(qubits, q)

        # ii) grover diffusion Z0 gate
        def grover_diffusion_operator(amplitudes):

            new_amplitudes = []

            for i in range(0, len(amplitudes)):

                if i < 2:
                    amp = amplitudes[i]
                else:
                    amp = -amplitudes[i]

                new_amplitudes.append(amp)

            return new_amplitudes

        qubits.manipulate(grover_diffusion_operator)

        # iii) hadamard top qubits
        for q in range(qubits.size(), 1, -1):
            hadamard_gate(qubits, q)

        it += 1

    # 5) measure
    print(qubits.measure_register_str())


def deutsch_jozsa(qubits, oracle_function):
    """
    Deutsch-Jozsa algorithm for determining whether a function is constant or balanced.
    It accepts input |x>|y>, where |x> can be either be a single qubit or a tensor product
    of qubits. If the function is constant, then |x> will be measured as all zeroes with a
    probability of unity. If it is balanced, then the opposite is true.
    :param qubits: the qubit register, consisting of n-1 input qubits, and 1 ancillary qubit
    :param oracle_function: a function that promises to be either constant or balanced,
    where it takes the qubit register |x>|y> and outputs |x>| (y + f(x))%2 >
    :return:
    """

    # 1) flip bottom qubit
    pauli_x_gate(qubits, 1)

    # 2) hadamard all qubits
    hadamard_gate(qubits)

    # 3) apply the function
    qubits.manipulate(oracle_function)

    # 4) hadamard top qubits
    for q in range(qubits.size(), 1, -1):
        hadamard_gate(qubits, q)

    # 5) measure qubits
    measured_register = qubits.measure_register_str()
    result = "constant"

    for i in range(0, len(measured_register) - 1):

        if measured_register[i] == "1":

            result = "balanced"
            break

    print("Function is " + result)

