import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Define system coefficients
num = [0.5, -0.8, 0.3]
den = [1.0, -1.8, 0.81]

# Compute zeros and poles
zeros = np.roots(num)
poles = np.roots(den)

# Print zeros and poles
print("Zeros:")
print(zeros)
print("Poles:")
print(poles)

# Check stability
stable = np.all(np.abs(poles) < 1)
print("Stability:", "Stable" if stable else "Unstable")

# Plot pole-zero diagram
plt.figure(figsize=(6,6))
theta = np.linspace(0, 2*np.pi, 400)
plt.plot(np.cos(theta), np.sin(theta), 'k--')  # Unit circle
plt.scatter(zeros.real, zeros.imag, s=80, facecolors='none', edgecolors='b', label='Zeros')
plt.scatter(poles.real, poles.imag, s=80, marker='x', color='r', label='Poles')
plt.title('Poles and Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.tight_layout()
plt.show()

# Frequency response
w, H = freqz(num, den, worN=1024)
mag_dB = 20 * np.log10(np.abs(H) + 1e-12)
phase_deg = np.unwrap(np.angle(H)) * 180 / np.pi

# Plot frequency response
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(w, mag_dB)
plt.title('Frequency Response')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(w, phase_deg)
plt.xlabel('Frequency (rad/sample)')
plt.ylabel('Phase (degrees)')
plt.grid(True)
plt.tight_layout()
plt.show()
