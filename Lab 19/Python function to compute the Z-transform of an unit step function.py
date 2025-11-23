import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def z_transform_unit_step(truncate=None):
    """Return symbolic Z-transform expression and finite truncated form (if specified)."""

    Z_expr = "1 / (1 - z^(-1))"
    ROC = "|z| > 1 (causal; ROC outside the outermost pole at z=1)"

    finite_expr = None
    if truncate is not None and int(truncate) >= 0:
        N = int(truncate)
        finite_expr = f"(1 - z^(-({N+1}))) / (1 - z^(-1))  (finite-sum N={N})"

    return Z_expr, ROC, finite_expr


def check_stability_from_roc(roc_description):
    """Check if ROC includes the unit circle => BIBO stable."""

    roc_description = roc_description.replace(" ", "").lower()

    # If ROC is outside |z| > 1 → unit circle (|z|=1) is NOT included → unstable
    if ">1" in roc_description and roc_description.startswith("|z|>"):
        return False

    # If ROC contains |z| < 1 → includes unit circle → stable
    if "<1" in roc_description:
        return True

    # Default conservative result
    return False


def pole_zero_plot_unit_step():
    """Plot unit circle and pole at z=1."""

    fig, ax = plt.subplots(figsize=(5, 5))
    theta = np.linspace(0, 2 * np.pi, 400)

    ax.plot(np.cos(theta), np.sin(theta), '--', lw=0.8, label='Unit Circle')
    ax.scatter([1], [0], marker='x', color='red', s=80, label='Pole at z=1')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('Re(z)')
    ax.set_ylabel('Im(z)')
    ax.set_title('Pole-Zero / ROC Visualization for u[n]')
    ax.grid(True, linestyle=':')
    ax.legend()
    plt.tight_layout()

    return fig, ax


def demo_truncated_response_and_freq(truncate=128):
    """Plot magnitude/phase response of truncated unit-step signal."""

    N = int(truncate)
    h = np.ones(N+1)

    w, H = freqz(h, [1], worN=1024)
    mag_db = 20 * np.log10(np.abs(H) + 1e-12)
    phase_deg = np.unwrap(np.angle(H)) * 180 / np.pi

    fig, axs = plt.subplots(2, 1, figsize=(9, 5), sharex=True)

    axs[0].plot(w, mag_db)
    axs[0].set_ylabel('Magnitude (dB)')
    axs[0].set_title(f'Freq Response of Truncated u[n] (Length={N+1})')
    axs[0].grid(True, linestyle=':')

    axs[1].plot(w, phase_deg)
    axs[1].set_ylabel('Phase (deg)')
    axs[1].set_xlabel('Frequency (rad/sample)')
    axs[1].grid(True, linestyle=':')

    plt.tight_layout()
    return fig, axs


if __name__ == "__main__":
    Z_expr, ROC, finite_expr = z_transform_unit_step(truncate=20)

    print("\n📌 Unilateral Z-transform of the causal unit-step u[n]:")
    print("   X(z) =", Z_expr)
    print("   Typical ROC:", ROC)

    if finite_expr is not None:
        print("\n📌 Finite-sum (N=20) closed-form:", finite_expr)

    stable = check_stability_from_roc(ROC)
    print("\n📌 Stability Check (BIBO):", "Stable (unit circle inside ROC)" if stable 
          else "Unstable (unit circle NOT included in ROC)")

    pole_zero_plot_unit_step()
    demo_truncated_response_and_freq(truncate=256)
    plt.show()
