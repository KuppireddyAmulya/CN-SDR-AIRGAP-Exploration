import numpy as np

# Parameters
samp_rate = 2000000  # 2MHz
duration = 1.0       # 1 second of data
freq = 100000        # 100kHz pulse
filename = "airgap_sim.iq"

# Create a bit pattern: 10101100 (The secret message)
bits = np.array([1, 0, 1, 0, 1, 1, 0, 0] * 10) 
samples_per_bit = int(samp_rate / 10) # Slow pulses for easy decoding

signal = np.array([], dtype=np.complex64)

for bit in bits:
    if bit == 1:
        # Create a "pulse" of noise/sine wave
        t = np.arange(samples_per_bit) / samp_rate
        pulse = 0.5 * np.exp(1j * 2 * np.pi * freq * t)
    else:
        # Create silence
        pulse = np.zeros(samples_per_bit, dtype=np.complex64)
    signal = np.append(signal, pulse)

# Save to file
signal.tofile(filename)
print(f"Success! Created {filename}")
