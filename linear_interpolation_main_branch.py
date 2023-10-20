import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Specify the path to your data file
data_file = "sawtooth_vert_sep_no_outliers_main_branch.txt"

# Load the data from the file
data = np.loadtxt(data_file)

# Separate the loaded data into x and y arrays
x_data = data[:, 0]
y_data = data[:, 1]

# Create an interpolation function
interp_func = interp1d(x_data, y_data, kind='linear', fill_value="extrapolate")

# Define the x interval for interpolated values
x_interval = np.arange(min(x_data), max(x_data) + 20, 10)  # Adjust the interval as needed

# Get the interpolated y values
y_interpolated = interp_func(x_interval)

# Print the interpolated values to a new data file
output_file = "interpolated_data_main_branch.txt"
with open(output_file, "w") as file:
    file.write("x, y\n")
    for x, y in zip(x_interval, y_interpolated):
        file.write(f"{x}, {y}\n")

# Plot the original data and the interpolated line
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label="Original Data", color='blue')
plt.plot(x_interval, y_interpolated, label="Interpolated Line", color='red')
plt.xlabel("Along-Strike Distance from South to North (m)")
plt.ylabel("Scarp Vertical Separation (m)")
plt.legend()
plt.title("Sawtooth Fault Scarp Displacement Distribution")
plt.grid(True)
plt.show()
