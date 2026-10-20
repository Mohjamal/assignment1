import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Task 2 Plot: Amdahl vs Gustafson
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

# ==========================================
# Task 4: Strong vs Weak Scaling
# ==========================================
p_task4 = np.array([1, 2, 4, 8, 16])
T_strong = np.array([100, 55, 30, 18, 12])
T_weak = np.array([100, 102, 105, 110, 120])

E_strong = T_strong[0] / (p_task4 * T_strong)
E_weak = T_weak[0] / T_weak

plt.figure(figsize=(8, 5))
plt.plot(p_task4, E_strong, marker='o', label='Strong Scaling Efficiency')
plt.plot(p_task4, E_weak, marker='s', label='Weak Scaling Efficiency')
plt.xlabel('Number of Processors (p)')
plt.ylabel('Efficiency')
plt.title('Strong vs Weak Scaling Efficiency')
plt.xticks(p_task4)
plt.ylim(0, 1.1)
plt.grid(True)
plt.legend()
plt.show()
