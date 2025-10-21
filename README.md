# Call Center Simulation 🚀

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple **M/M/c queue simulation** of a call center using **SimPy**, designed for learning and experimentation in **performance modeling**. Ideal for university projects, labs, or self-study.

---

## 🔧 Quick Start Guide

### 1. Install Dependencies
Make sure you have Python installed, then run:

```bash
pip install simpy pandas matplotlib
```

### 2. Run the Simulation

```bash
python call_center_simpy.py
```

### 3. View Results
The script automatically generates the following files:

| File | Description |
|------|-------------|
| `simpy_results_summary.csv` | Key performance metrics (average waiting time, queue length, agent utilization, etc.) |
| `plot_avg_wait.png` | Comparison of average waiting times across different scenarios |
| `plot_utilization.png` | Agent utilization comparison |
| `hist_waits.png` | Histogram of individual call waiting times |

---

## ⚙ Features

- **Multi-agent (M/M/c) queue simulation**
- **Customizable parameters:** number of agents, arrival rates, and service rates
- **Visualization of performance metrics:** plots and histograms for analysis
- **Academic-friendly:** ideal for assignments, labs, and self-study

---

## 📊 Understanding the Results

### Key Metrics

| Metric | Description | Ideal Value |
|--------|-------------|-------------|
| **avg_wait** | Average time customers spend waiting in queue | Lower is better |
| **utilization** | Percentage of time agents are busy | 70-85% optimal |
| **throughput** | Number of calls completed per time unit | Higher is better |

---

## 🎯 Experiment Scenarios

The simulation includes 5 pre-configured scenarios:

| Scenario | Arrival Rate (λ) | Service Rate (μ) | Agents (c) | Purpose |
|----------|------------------|------------------|------------|---------|
| **BaseSystem_C2** | 4.0 | 1.0 | 2 | Baseline with minimal agents |
| **BaseSystem_C4** | 4.0 | 1.0 | 4 | Increased capacity |
| **BaseSystem_C8** | 4.0 | 1.0 | 8 | Maximum capacity |
| **HigherLoad_C4** | 6.0 | 1.0 | 4 | Testing under heavy load |
| **FasterService_C4** | 4.0 | 1.25 | 4 | Improved service speed |

---

## 🛠 Customization

### Modify Scenarios
Edit the `scenarios` list in `call_center_simpy.py`:

```python
scenarios = [
    {"label": "MyScenario", "lambda": 5.0, "mu": 1.5, "servers": 3},
]
```

**Parameters:**
- `lambda`: Call arrival rate (calls per time unit)
- `mu`: Service rate (calls handled per agent per time unit)
- `servers`: Number of agents

### Adjust Simulation Duration
Change the simulation time (default: 3000 time units):

```python
metrics = run_simpy_simulation(s["lambda"], s["mu"], s["servers"], sim_time=5000)
```

---

## 📈 Sample Results

| Scenario | Avg Wait Time | Utilization | Throughput |
|----------|--------------|-------------|------------|
| BaseSystem_C2 | 750.61 | 100.0% | 1.967 |
| BaseSystem_C4 | 12.74 | 98.2% | 3.964 |
| BaseSystem_C8 | 0.018 | 51.1% | 4.023 |
| HigherLoad_C4 | 490.62 | 100.0% | 3.997 |
| FasterService_C4 | 0.756 | 82.9% | 4.100 |

---

## 📚 Learn More

### What is M/M/c?
- **M:** Markovian (exponential) arrival times
- **M:** Markovian (exponential) service times
- **c:** Number of parallel servers (agents)

### Stability Condition
For a stable system: **λ < c × μ**

Example:
- λ = 4, μ = 1, c = 2
- Traffic intensity: ρ = 4 / (2 × 1) = 2.0 ❌ **Unstable!**
- Need at least 5 agents: 4 / (5 × 1) = 0.8 ✓ **Stable**

---

## 🎓 Academic Information

**Course:** EEX5362 - Performance Modelling  
**Institution:** The Open University of Sri Lanka  
**Level:** Bachelor of Software Engineering Honours - Level 5  
**Academic Year:** 2024/2025

---

## 👤 Author

**MBNM NASHEETH**  
Student ID: 321426009

---

## 📄 License

This project is available under the MIT License for educational purposes.

---

## 🤝 Contributing

Feel free to fork this repository and experiment with different scenarios. Suggestions and improvements are welcome!

---


**Happy Simulating! 🎉**
