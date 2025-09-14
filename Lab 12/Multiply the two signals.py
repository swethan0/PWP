import numpy as np
import matplotlib.pyplot as plt
fs = 500
t = np.linspace(0, 2, 2*fs, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t)
cosine_10 = np.cos(2 * np.pi * 10 * t)
multiplied_signal = sine_5 * cosine_10

plt.figure(figsize=(10, 4))
plt.plot(t, multiplied_signal, label="Sine(5Hz) * Cosine(10Hz)")
plt.title("(b) Product of 5 Hz Sine and 10 Hz Cosine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


