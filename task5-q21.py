import numpy as np
import matplotlib.pyplot as plt

# 1. The Dataset
p_vals = np.array([1, 2, 4, 8, 16, 32, 64, 128])
times = np.array([
    [240.0, 238.5, 241.2, 239.8, 240.5],
    [122.5, 121.0, 123.2, 121.8, 122.0],
    [63.0, 62.2, 63.8, 62.5, 63.1],
    [33.5, 32.8, 34.0, 33.1, 33.6],
    [18.9, 18.4, 19.2, 18.6, 18.8],
    [12.5, 12.1, 12.9, 12.3, 12.6],
    [9.8, 9.4, 10.1, 9.6, 9.9],
    [8.7, 8.3, 9.0, 8.5, 8.8]
])

# 2. Calculate Mean and Sample Standard Deviation
means = np.mean(times, axis=1)
stds = np.std(times, axis=1, ddof=1)

# 3. Calculate Speedup and Efficiency
t1_mean, t1_std = means[0], stds[0]
speedups = t1_mean / means
efficiencies = speedups / p_vals

# 4. Error Propagation
speedup_errs = speedups * np.sqrt((t1_std/t1_mean)**2 + (stds/means)**2)
efficiency_errs = speedup_errs / p_vals

# 5. Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Speedup Plot
ax1.errorbar(p_vals, speedups, yerr=speedup_errs, fmt='-o', capsize=5, color='b', ecolor='black')
ax1.set_xscale('log', base=2)
ax1.set_xticks(p_vals)
ax1.set_xticklabels(p_vals)
ax1.set_xlabel('Number of Processors (p) [Log Scale]')
ax1.set_ylabel('Speedup S(p)')
ax1.set_title('Speedup vs. Processors (with Error Bars)')
ax1.grid(True, which="both", ls="--", alpha=0.7)

# Efficiency Plot
ax2.errorbar(p_vals, efficiencies, yerr=efficiency_errs, fmt='-s', capsize=5, color='orange', ecolor='black')
ax2.set_xscale('log', base=2)
ax2.set_xticks(p_vals)
ax2.set_xticklabels(p_vals)
ax2.set_xlabel('Number of Processors (p) [Log Scale]')
ax2.set_ylabel('Efficiency E(p)')
ax2.set_title('Efficiency vs. Processors (with Error Bars)')
ax2.set_ylim(0, 1.1)
ax2.grid(True, which="both", ls="--", alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.show()