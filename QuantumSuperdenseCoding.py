#Superdense Coding, getting two bits from one qubit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import compile, Aer
from qiskit.exceptions import QiskitError
from math import pi

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

#make two entangled bits
qc.h(qr[0])
qc.cx(qr[0], qr[1])

#send qubit 0 to reciever to encode
qc.x(qr[0])
qc.z(qr[0])

#send qubit 0 back to undo the entanglement
qc.cx([qr[0], qr[1]])
qc.h(qr[0])

#measure to get two classical bits
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

backend = Aer.get_backend('qasm_simulator')
qobj = compile(qc, backend, shots=1000)
job = backend.run(qobj)
result = job.result()
counts = result.get_counts()
print(counts)
input("")