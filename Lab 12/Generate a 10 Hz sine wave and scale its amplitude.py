import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_10 = np.sin(2 * np.pi * 10 * t)
scaled_sine = 3 * sine_10

plt.figure(figsize=(10, 4))
plt.plot(t, sine_10, label="Original 10 Hz Sine")
plt.plot(t, scaled_sine, label="Scaled by 3")
plt.title("(d) Scaled 10 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


