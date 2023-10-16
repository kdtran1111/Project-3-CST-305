#Kevin Tran


import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f1(x):
    return (-1/8) * np.sin(2 * x) + (1/4) * x

def f2(x):
    return 4 * (1 - np.cos(x))

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values for both functions
y1 = f1(x)
y2 = f2(x)

# Plot the functions
plt.plot(x, y1, label="ODE 1")
plt.plot(x, y2, label="ODE 2", linestyle='--')

# Setting the title and labels
plt.title("Plot of the given functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


#Plotting the Green's function result

# Generate t values
t = np.linspace(-10, 10, 400)  # Generates 1000 points between 0 and 10

# Calculate the y values for each function
y1 = (-1/8)*np.sin(2*t) + (1/4)*t
y2 = 4*(1-np.cos(t))

# Plot the first function
plt.plot(t, y1, label='ODE 1 Green')

# Plot the second function
plt.plot(t, y2, label='ODE 2 Green')

# Set title and labels
plt.title('Plot of the given functions')
plt.xlabel('t')
plt.ylabel('y')

# Show legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()


# In[ ]:




