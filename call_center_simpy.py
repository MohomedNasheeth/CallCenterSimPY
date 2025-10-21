# call_center_simpy.py
# SimPy-based Call Center Simulation (M/M/c Queue Model)
# -------------------------------------------------------
# This script simulates a call center with multiple agents using SimPy.
# It measures system performance metrics like average waiting time,
# agent utilization, and throughput under multiple scenarios.

import simpy
import random
import statistics
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)

# Define a single customer process
def customer(env, name, call_center, service_rate, wait_times, busy_time_tracker):
    arrival_time = env.now
    with call_center.request() as request:
        yield request
        wait = env.now - arrival_time
        wait_times.append(wait)
        service_time = random.expovariate(service_rate)
        busy_time_tracker.append(service_time)
        yield env.timeout(service_time)

# Define the arrival process
def arrival_process(env, arrival_rate, call_center, service_rate, wait_times, busy_time_tracker):
    i = 0
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        i += 1
        env.process(customer(env, f"Caller_{i}", call_center, service_rate, wait_times, busy_time_tracker))

# Run the simulation
def run_simpy_simulation(arrival_rate, service_rate, num_agents, sim_time=2000):
    env = simpy.Environment()
    call_center = simpy.Resource(env, capacity=num_agents)
    wait_times = []
    busy_time_tracker = []

    env.process(arrival_process(env, arrival_rate, call_center, service_rate, wait_times, busy_time_tracker))
    env.run(until=sim_time)

    avg_wait = statistics.mean(wait_times) if wait_times else 0
    utilization = (sum(busy_time_tracker) / (num_agents * sim_time)) if sim_time > 0 else 0
    throughput = len(busy_time_tracker) / sim_time

    return {
        "avg_wait": avg_wait,
        "utilization": utilization,
        "throughput": throughput,
        "wait_times": wait_times
    }

# Define scenarios
scenarios = [
    {"label": "BaseSystem_C2", "lambda": 4.0, "mu": 1.0, "servers": 2},
    {"label": "BaseSystem_C4", "lambda": 4.0, "mu": 1.0, "servers": 4},
    {"label": "BaseSystem_C8", "lambda": 4.0, "mu": 1.0, "servers": 8},
    {"label": "HigherLoad_C4", "lambda": 6.0, "mu": 1.0, "servers": 4},
    {"label": "FasterService_C4", "lambda": 4.0, "mu": 1.25, "servers": 4},
]

# Run simulations
results = []
all_waits = {}

for s in scenarios:
    metrics = run_simpy_simulation(s["lambda"], s["mu"], s["servers"], sim_time=3000)
    results.append({
        "scenario": s["label"],
        "lambda": s["lambda"],
        "mu": s["mu"],
        "servers": s["servers"],
        "avg_wait": metrics["avg_wait"],
        "utilization": metrics["utilization"],
        "throughput": metrics["throughput"]
    })
    all_waits[s["label"]] = metrics["wait_times"]

df = pd.DataFrame(results)
print("\nSimulation Results Summary:\n", df)

# Plot 1: Average waiting time
plt.figure(figsize=(8,4))
plt.bar(df["scenario"], df["avg_wait"], color="skyblue")
plt.title("Average Waiting Time by Scenario")
plt.ylabel("Average Wait (time units)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_avg_wait.png")
plt.show()

# Plot 2: Utilization
plt.figure(figsize=(8,4))
plt.bar(df["scenario"], df["utilization"], color="orange")
plt.title("Server Utilization by Scenario")
plt.ylabel("Utilization (fraction)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_utilization.png")
plt.show()

# Plot 3: Wait time histograms
plt.figure(figsize=(10,8))
for i, s in enumerate(all_waits.keys(), start=1):
    plt.subplot(3,2,i)
    plt.hist(all_waits[s], bins=30, color="gray", edgecolor="black")
    plt.title(s)
    plt.xlabel("Wait time")
    plt.ylabel("Count")
plt.tight_layout()
plt.savefig("hist_waits.png")
plt.show()

# Save results
df.to_csv("simpy_results_summary.csv", index=False)
print("\nSaved outputs:")
print("- results_summary.csv")
print("- plot_avg_wait.png")
print("- plot_utilization.png")
print("- hist_waits.png")
print("\nDone.")
