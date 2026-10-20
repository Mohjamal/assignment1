import matplotlib.pyplot as plt

# 1. Define the data from Part 1
p_values = [1, 2, 4, 8, 16, 64, 1024]
s_05_speedup_values = [1.000, 1.905, 3.478, 5.926, 9.143, 15.422, 19.636]

# 2. Create the plot
plt.figure(figsize=(8, 5))
plt.plot(p_values, s_05_speedup_values, marker='o', linestyle='-', color='b', label='s = 0.05')

# 3. Set the x-axis to a log scale (Base 2)
plt.xscale('log', base=2)

# 4. Add labels, title, and grid
plt.xlabel('Number of Processors (p) [Log Scale Base 2]')
plt.ylabel('Speedup S(p)')
plt.title("Amdahl's Law: Speedup vs. Processors (s=0.05)")
plt.xticks(p_values, labels=p_values) # Forces x-axis to show actual p values instead of 10^x
plt.grid(True, which="both", ls="--", alpha=0.7)
plt.legend()

# 5. Show the plot
plt.show()