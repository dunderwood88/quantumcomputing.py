from qubit_manipulators import *
from qubit_register import *
from quantum_algorithms import *

qreg = QubitRegister(3)

qft(qreg)


"""def balanced_function(amplitudes):

    new_amplitudes = []

    for i in range(0, len(amplitudes)):

        if i == 4:
            amp = amplitudes[5]
        elif i == 5:
            amp = amplitudes[4]
        elif i == 6:
            amp = amplitudes[7]
        elif i == 7:
            amp = amplitudes[6]
        else:
            amp = amplitudes[i]

        new_amplitudes.append(amp)

    return new_amplitudes


def constant_function(amplitudes):

    new_amplitudes = []

    for i in range(0, len(amplitudes)):

        amp = amplitudes[i]

        new_amplitudes.append(amp)

    return new_amplitudes


deutsch_jozsa(qreg, constant_function)


def search_space(amplitudes):

    new_amplitudes = []

    for i in range(0, len(amplitudes)):

        if i == 6:
            amp = amplitudes[7]
        elif i == 7:
            amp = amplitudes[6]
        else:
            amp = amplitudes[i]

        new_amplitudes.append(amp)

    return new_amplitudes


grover_search(qreg, search_space)"""






