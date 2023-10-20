import numpy as np
import matplotlib.pyplot as plt

# Specify the input data file for moving average
input_file0 = "interpolated_data_main_branch.txt"

# Load the data from the input file
data0 = np.loadtxt(input_file0, delimiter=',')

# Separate the loaded data into x and y arrays
x_data0 = data0[:, 0]
y_data0 = data0[:, 1]

# Specify the input data file for moving average
input_file1 = "interpolated_data_east_branch.txt"

# Load the data from the input file
data1 = np.loadtxt(input_file1, delimiter=',')

# Separate the loaded data into x and y arrays
x_data1 = data1[:, 0]
y_data1 = data1[:, 1]

# Specify the input data file for Holocene scarp profiles
input_file2 = "holocene_profiles.txt"

# Load the data from the input file
data2 = np.loadtxt(input_file2, delimiter=',')

# Separate the loaded data into x, y, and z arrays
x_data2 = data2[:, 0]
y_data2 = data2[:, 1]
y_error2 = data2[:, 2]

# Specify the input data file for Holocene scarp profiles
input_file3 = "pleistocene_profiles.txt"

# Load the data from the input file
data3 = np.loadtxt(input_file3, delimiter=',')

# Separate the loaded data into x, y, and z arrays
x_data3 = data3[:, 0]
y_data3 = data3[:, 1]
y_error3 = data3[:, 2]

# Specify the input data file for Holocene scarp profiles
input_file4 = "quaternary_profiles.txt"

# Load the data from the input file
data4 = np.loadtxt(input_file4, delimiter=',')

# Separate the loaded data into x, y, and z arrays
x_data4 = data4[:, 0]
y_data4 = data4[:, 1]
y_error4 = data4[:, 2]

# Specify the input data file for Holocene scarp profiles
input_file5 = "outlier_profiles.txt"

# Load the data from the input file
data5 = np.loadtxt(input_file5, delimiter=',')

# Separate the loaded data into x, y, and z arrays
x_data5 = data5[:, 0]
y_data5 = data5[:, 1]
y_error5 = data5[:, 2]

# # Specify the input data file for summed branches
# input_file6 = "moving_average_data_summed_branches.txt"

# # Load the data from the input file
# data6 = np.loadtxt(input_file6, delimiter=',')

# # Separate the loaded data into x, y arrays
# x_data6 = data6[:, 0]
# y_data6 = data6[:, 1]

# Define the moving average window size (in meters)
window_size = 2000

# # Calculate the moving average on main branch without cropping data
# moving_average_main = np.convolve(y_data0, np.ones(window_size) / window_size, mode='full')[:len(y_data0)]

# Calculate the moving average on main branch with padding at the beginning
padding_value = 0  # You can adjust this value as needed
padded_y_data0 = np.pad(y_data0, (window_size // 2, 0), mode='constant', constant_values=padding_value)
moving_average_main = np.convolve(padded_y_data0, np.ones(window_size) / window_size, mode='full')[:len(padded_y_data0)]
# Calculate the moving average on main branch without cropping data

# Adjust x_data0 to have the same length as moving_average_main
x_data0 = x_data0[:len(moving_average_main)]

# Create a new data file for the moving average
output_file = "moving_average_data_main_branch_test.txt"
with open(output_file, "w") as file:
    file.write("x, y\n")
    for x, avg_y in zip(x_data0, moving_average_main):
        file.write(f"{x}, {avg_y}\n")

# Calculate the moving average on east branch without cropping data
padding_value = 0  # You can adjust this value as needed
padded_y_data1 = np.pad(y_data1, (window_size // 2, 0), mode='constant', constant_values=padding_value)
moving_average_east = np.convolve(y_data1, np.ones(window_size) / window_size, mode='full')[:len(padded_y_data1)]

# Create a new data file for the moving average
output_file = "moving_average_data_east_branch_test.txt"
with open(output_file, "w") as file:
    file.write("x, y\n")
    for x, avg_y in zip(x_data1, moving_average_east):
        file.write(f"{x}, {avg_y}\n")

# Plot the original data and the moving average line
plt.figure(figsize=(8, 6))
# plt.scatter(x_data2, y_data2, label="Holocene Scarps", color='blue', alpha=0.5, marker='o', s=10)
# plt.scatter(x_data3, y_data3, label="Holocene Scarps", color='green', alpha=0.5, marker='o', s=10)
# plt.scatter(x_data4, y_data4, label="Holocene Scarps", color='orange', alpha=0.5, marker='o', s=10)
# plt.scatter(x_data5, y_data5, label="Holocene Scarps", color='yellow', alpha=0.5, marker='o', s=10)
plt.errorbar(x_data2, y_data2, yerr=y_error2, fmt='o', label="Holocene Scarps", color='blue', alpha=0.5)
plt.errorbar(x_data3, y_data3, yerr=y_error3, fmt='o', label="Pleistocene Scarps", color='green', alpha=0.5)
plt.errorbar(x_data4, y_data4, yerr=y_error4, fmt='o', label="Quaternary Scarps", color='orange', alpha=0.5)
plt.errorbar(x_data5, y_data5, yerr=y_error5, fmt='o', label="Outliers not Included in Moving Average", color='black', alpha=0.5)
plt.plot(x_data0, moving_average_main, label=f"Main Branch Moving Average (Window Size {window_size} m)", color='red')
plt.plot(x_data1, moving_average_east, label=f"East Branch Moving Average (Window Size {window_size} m)", color='gray')
# plt.plot(x_data6, y_data6, label=f"Summed Branches Moving Average (Window Size {window_size} m)", color='purple', linestyle='dashed')
plt.ylim(-1, 20)
plt.xlabel("Distance Along Fault From South to North (m)")
plt.ylabel("Vertical Separation (m)")
plt.legend()
plt.title("Moving Average of Vertical Separation")
plt.grid(True)
plt.show()
