import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_original = np.sin(2 * np.pi * 5 * t)
sine_shifted = np.sin(2 * np.pi * 5 * (t - 0.1))

plt.figure(figsize=(10, 4))
plt.plot(t, sine_original, label="Original 5 Hz Sine")
plt.plot(t, sine_shifted, label="Shifted by 0.1s")
plt.title("(c) Time Shifted 5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


