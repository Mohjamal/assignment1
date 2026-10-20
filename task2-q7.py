import numpy as np
import matplotlib.pyplot as plt

p_vals = np.array([1, 2, 4, 8, 16, 64, 1024])

plt.subplot(1, 2, 2)
s_val = 0.05
S_amdahl = 1 / (s_val + (1 - s_val) / p_vals)
S_gustafson = s_val + p_vals * (1 - s_val)

plt.plot(p_vals, S_amdahl, marker='o', label="Amdahl's (s=0.05)")
plt.plot(p_vals, S_gustafson, marker='s', label="Gustafson's (s=0.05)")
plt.xscale('log', base=2)
plt.xlabel('Number of Processors (p)')
plt.ylabel('Speedup S(p)')
plt.title("Amdahl's vs Gustafson's Law")
plt.grid(True, which="both", ls="--")
plt.legend()

plt.tight_layout()
plt.show()
