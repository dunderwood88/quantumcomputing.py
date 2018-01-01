from math import *
import cmath


def hadamard_gate(qubits, qubit_position=None):
    """
    Accepts a qubit register object and performs a Hadamard
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

            diff_coeff = int(pow(2, qubit_position)/2)

            if count == diff_coeff:
                minus = not minus
                count = 0

            if not minus:
                amp = (amplitudes[i] + amplitudes[i + diff_coeff]) / sqrt(2)
            else:
                amp = (amplitudes[i - diff_coeff] - amplitudes[i]) / sqrt(2)

            new_amplitudes.append(amp)
            count += 1

        return new_amplitudes

    qubits.manipulate(hadamard_function)


def pauli_x_gate(qubits, qubit_position=None):
    """
        Accepts a qubit register object and performs a pauli-X
        transform on the qubit in the position specified

        :param qubits: the qubit vector
        :param qubit_position: the register position of the qubit to be transformed
        """

    # if no qubit position specified, apply to all qubits
    if qubit_position is None:

        for i in range(1, qubits.size() + 1):
            pauli_x_gate(qubits, i)

        return

    if qubit_position < 1 or qubit_position > qubits.size():
        print("Invalid position (" + qubit_position
              + ") for register of size " + qubits.size())

        return

    def pauli_x_function(amplitudes):

        new_amplitudes = []
        minus = False
        count = 0

        for i in range(0, len(amplitudes)):

            diff_coeff = int(pow(2, qubit_position) / 2)

            if count == diff_coeff:
                minus = not minus
                count = 0

            if not minus:
                amp = amplitudes[i + diff_coeff]
            else:
                amp = amplitudes[i - diff_coeff]

            new_amplitudes.append(amp)
            count += 1

        return new_amplitudes

    qubits.manipulate(pauli_x_function)


def pauli_y_gate(qubits, qubit_position=None):
    """
        Accepts a qubit register object and performs a pauli-Y
        transform on the qubit in the position specified

        :param qubits: the qubit vector
        :param qubit_position: the register position of the qubit to be transformed
        """

    # if no qubit position specified, apply to all qubits
    if qubit_position is None:

        for i in range(1, qubits.size() + 1):
            pauli_y_gate(qubits, i)

        return

    if qubit_position < 1 or qubit_position > qubits.size():
        print("Invalid position (" + qubit_position
              + ") for register of size " + qubits.size())

        return

    def pauli_y_function(amplitudes):

        new_amplitudes = []
        minus = False
        count = 0

        for i in range(0, len(amplitudes)):

            diff_coeff = int(pow(2, qubit_position) / 2)

            if count == diff_coeff:
                minus = not minus
                count = 0

            if not minus:
                im = complex(0, -1)
                amp = im * amplitudes[i + diff_coeff]
            else:
                im = complex(0, 1)
                amp = im * amplitudes[i - diff_coeff]

            new_amplitudes.append(amp)
            count += 1

        return new_amplitudes

    qubits.manipulate(pauli_y_function)


def pauli_z_gate(qubits, qubit_position=None):
    """
        Accepts a qubit register object and performs a pauli-Z
        transform on the qubit in the position specified

        :param qubits: the qubit vector
        :param qubit_position: the register position of the qubit to be transformed
        """

    # if no qubit position specified, apply to all qubits
    if qubit_position is None:

        for i in range(1, qubits.size() + 1):
            pauli_z_gate(qubits, i)

        return

    if qubit_position < 1 or qubit_position > qubits.size():
        print("Invalid position (" + qubit_position
              + ") for register of size " + qubits.size())

        return

    def pauli_z_function(amplitudes):

        new_amplitudes = []
        minus = False
        count = 0

        for i in range(0, len(amplitudes)):

            diff_coeff = int(pow(2, qubit_position) / 2)

            if count == diff_coeff:
                minus = not minus
                count = 0

            if not minus:
                amp = amplitudes[i]
            else:
                amp = -amplitudes[i]

            new_amplitudes.append(amp)
            count += 1

        return new_amplitudes

    qubits.manipulate(pauli_z_function)


def qft(qubits):
    """
    Quantum analogue of the discrete fourier transform. Performs the linear transformation
    on an input verctor of qubits.

    :param qubits: the input qubit vector to be fourier transformed
    """

    def qft_function(amplitudes):

        new_amplitudes = []
        num_points = len(amplitudes)

        # for each element in the transformed vector
        for i in range(0, num_points):

            summation = complex(0, 0)

            # for each element in the input vector
            for j in range(0, num_points):

                angle = (2.0 * pi * i * j)/num_points

                summation += amplitudes[j] * cmath.exp(-1j * angle)

            new_amplitudes.append(summation)

        print(new_amplitudes)

        return new_amplitudes

    qubits.manipulate(qft_function)


