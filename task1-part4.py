import numpy as np
import matplotlib.pyplot as plt

p_vals = np.array([1, 2, 4, 8, 16, 64, 1024])
s_list = [0.05, 0.10, 0.20]

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
for s in s_list:
    speedup = 1 / (s + (1 - s) / p_vals)
    plt.plot(p_vals, speedup, marker='o', label=f'Amdahl s={s}')
plt.xscale('log', base=2)
plt.xlabel('Number of Processors (p)')
plt.ylabel('Speedup S(p)')
plt.title("Amdahl's Law Scaling")
plt.grid(True, which="both", ls="--")
plt.legend()
