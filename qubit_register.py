from random import *


class QubitRegister:

    def __init__(self, num_qubits=None):
        """
        Constructor
        :param numQubits: the size of the register/the number of qubits to initialize. Default = 1
        """

        if num_qubits is None:
            self.__num_qubits = 1
        else:
            self.__num_qubits = num_qubits

        self.__qubit_amplitudes = []

        state = "|"

        for i in range(0, pow(2, self.__num_qubits)):

            if i == 0:
                self.__qubit_amplitudes.append(complex(1, 0))
            else:
                self.__qubit_amplitudes.append(complex(0, 0))

            if i < self.__num_qubits:
                state += "0"

        print("Initialized qubit register in " + state + "> state")

    def size(self):
        """
        Get the size of the current register
        :return: the integer size of the register
        """
        return self.__num_qubits

    def manipulate(self, manipulation):
        """
        Accepts a function which performs a manipulation on the qubit register state.
        Manipulations accept a qubit system (single or register) object and pass into it
        a function which performs an internal manipulation, which avoids exposing the internal
        information of the qubit
        :param manipulation: function which accepts a complex number vector
        """

        new_amplitudes = manipulation(self.__qubit_amplitudes)

        # check for unitarity, i.e. |a|^2 + |b|^2 + ... = 1
        summation = 0.0

        for amp in new_amplitudes:
            summation += pow(abs(amp), 2)

        if 1 - summation < 1E-3:
            self.__qubit_amplitudes = new_amplitudes

    def __random_state(self):
        """
        Gets a single random state from the superposition based
        on the individual state probability amplitudes

        :return: the position of the random state in the summation
        """

        state_pos = 0
        total_prob = pow(abs(self.__qubit_amplitudes[0]), 2)
        rand = random()

        while total_prob < rand and state_pos < pow(2, self.__num_qubits) - 1:
            state_pos += 1
            total_prob += pow(abs(self.__qubit_amplitudes[state_pos]), 2)

        return state_pos

    def measure_register_int(self):
        """
        Performs a measurement on the qubit register in the computational basis
        :return: an integer representing the base10 value of the collapsed classical state
        """

        state = self.__random_state()
        i = 0

        # collapse the wavefunction
        while i < pow(2, self.__num_qubits):

            if i == state:
                self.__qubit_amplitudes[i] = 1.0
            else:
                self.__qubit_amplitudes[i] = 0.0

            i += 1

        return state

    def measure_register_str(self):
        """
        Performs a measurement on the qubit register in the computational basis
        :return: a string of binary digits representing a collapsed classical state
        """

        state = self.measure_register_int()
        i = 0
        output = ""

        while i < self.__num_qubits:
            output = str((state >> i) & 1) + output
            i += 1

        return output


class Qubit(QubitRegister):

    def __init__(self):
        """
        Constructor
        """
        QubitRegister.__init__(self, 1)

