import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t)
reversed_sine = sine_5[::-1]

plt.figure(figsize=(10, 4))
plt.plot(t, sine_5, label="Original 5 Hz Sine")
plt.plot(t, reversed_sine, label="Time-Reversed 5 Hz Sine")
plt.title("(e) Time Reversal of 5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

