# Simulated Annealing for Covering Arrays

This project implements a Simulated Annealing-based approach to generate covering arrays for combinatorial software testing. The objective is to efficiently cover all pairwise parameter combinations while minimizing the number of test cases.

## 🔍 Project Overview
- **Algorithm**: Simulated Annealing
- **Language**: Python
- **Problem**: Covering Array (CA(N; t, k, v)) generation with strength t = 2, v = 2, and varying k
- **Applications**: Combinatorial software testing, optimization

## 📁 Files Included
- `covering_array_sa.py`: Python implementation of the SA algorithm
- `project_report.pdf`: Documentation and analysis of results

## 🧠 Key Features
- Custom cooling schedule and acceptance criteria
- Dynamic N based on number of parameters (k)
- Output: Test matrix covering all pairwise combinations

## 🧪 Sample Execution
```bash
python covering_array_sa.py
