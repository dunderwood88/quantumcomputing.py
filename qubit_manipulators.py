import math


def hadamard_gate(qubits, qubit_position=None):
    """
    Accepts a qubit register object reference and performs a Hadamard
    transform on the qubit in the position specified

    :param qubits: the qubit vector
    :param qubit_position: the register position of the qubit to be transformed
    """

    # if no qubit position specified, apply to all qubits
    if qubit_position is None:

        for i in range(1, qubits.size() + 1):
            hadamard_gate(qubits, i)

        return

    if qubit_position < 1 or qubit_position > qubits.size():

        print("Invalid position (" + qubit_position
              + ") for register of size " + qubits.size())

        return

    def hadamard_function(amplitudes):

        new_amplitudes = []
        minus = False
        count = 0

        for i in range(0, len(amplitudes)):

            diff_coeff = pow(2, qubit_position)/2

            if count == diff_coeff:
                minus = not minus
                count = 0

            if not minus:
                amp = (amplitudes[i] + amplitudes[i + diff_coeff]) / math.sqrt(2)
            else:
                amp = (amplitudes[i - diff_coeff] - amplitudes[i]) / math.sqrt(2)

            new_amplitudes.append(amp)
            count += 1

        return new_amplitudes

    qubits.manipulate(hadamard_function)

