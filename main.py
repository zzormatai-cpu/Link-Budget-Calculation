import numpy as np
import matplotlib.pyplot as plt

# Frequency (Hz)
f = 3.5e9  # 3.5 GHz (5G)

# Distance range (meters)
distances = np.linspace(10, 5000, 200)

# Constants
c = 3e8

def fspl(f, d):
    return 20 * np.log10(4 * np.pi * d * f / c)

# Transmit power (dBm)
tx_power = 30

# Calculate path loss and received power
path_loss = fspl(f, distances)
rx_power = tx_power - path_loss

# Plot
plt.figure()

plt.plot(distances, rx_power, label="Received Power (dBm)")
plt.axhline(y=-90, color='r', linestyle='--', label="Receiver Sensitivity")

plt.xlabel("Distance (m)")
plt.ylabel("Power (dBm)")
plt.title("5G Link Budget vs Distance")
plt.grid()
plt.legend()

plt.show()