# 🧮 MPI Distributed Monte Carlo Simulation

This project uses `mpi4py` (Python bindings for MPI) to estimate the value of π via a distributed Monte Carlo method. The computation is split across multiple processes to demonstrate parallel programming using MPI.

---

## 📂 Project Structure

```
mpi-distributed-computing/
├── main.py # Main MPI-based Monte Carlo estimator
├── README.md # Project documentation
├── .gitignore
└── .idea/ # (optional) IDE settings
```

---

## 📊 How It Works

1. **Monte Carlo Method:**
   - Generate random 2D points `(x, y)` in the unit square `[0, 1]^2`
   - Count how many satisfy: `x^2 + y^2 <= 1`
   - Estimate π using: `π ≈ 4 × (points inside circle / total points)`

2. **Parallel Execution with MPI:**
   - **Rank 0 (master):**
     - Generates \(N = 1,000,000\) points
     - Splits them evenly among all worker processes
     - Sends chunks using `comm.send()`
     - Receives partial results via `comm.recv()` and aggregates them
   - **Worker Ranks (>0):**
     - Receive a chunk of coordinates
     - Run the `monte_carlo()` function on their part
     - Send partial estimate back to master

---

## 🔧 Requirements

- Python 3.8+
- `mpi4py` (install via pip)
- MPI runtime (e.g. OpenMPI or MPICH)

### Installation

```bash
pip install mpi4py
```
---

## 🚀 Running the Simulation

Use mpirun to run with multiple processes:

```bash
mpirun -n 4 python main.py
```

### 📌 Here:

-n 4 means 4 processes: 1 master + 3 workers

Output will show each process and the estimated π values

🧠 Key Functions

`generate_arrays(N, m)`
- Generates N random 2D points
- Returns m equally-sized slices

`monte_carlo(arr)`
- Counts points inside the unit circle
- Returns an estimate of π for a given slice
