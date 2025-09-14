import numpy as np
import matplotlib.pyplot as plt
fs = 1000  # sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t)
sine_10 = np.sin(2 * np.pi * 10 * t)
added_signal = sine_5 + sine_10

plt.figure(figsize=(10, 4))
plt.plot(t, added_signal, label="5 Hz + 10 Hz")
plt.title("(a) Sum of 5 Hz and 10 Hz Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

