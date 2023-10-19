from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

# Create a quantum circuit with 4 qubits
qc = QuantumCircuit(4, 4)

# Apply Hadamard gate (qubit 0)
qc.h(0)

# Entangle the qubits with CNOT
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)

# Measure all qubits
qc.measure_all()

# Simulate the circuit on a local simulator
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots = 1024)

# Result
result = job.result()
counts = result.get_counts(qc)

print(counts)


