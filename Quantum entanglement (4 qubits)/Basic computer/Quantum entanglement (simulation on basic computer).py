from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, circuit_drawer

# Create a Quantum Circuit with 4 qubits
qc = QuantumCircuit(4, 4)

# Apply Hadamard gate to the first qubit (qubit 0)
qc.h(0)

# Apply CNOT gates to entangle the qubits
qc.cx(0, 1)
qc.cx(0, 2)
qc.cx(0, 3)

# Map the quantum measurement to the classical bits
qc.measure([0,1,2,3],[0,1,2,3])

print("The quantum circuit:")
circuit_drawer(qc, output='mpl')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(qc)

print("\nTotal count for 0000 and 1111 are:",counts)

# Also you might use module 'histogram' from Qiskit to make a vizualization
