**Air-Gap Side-Channel Exfiltration Project**
**1. Overview**
This project demonstrates a Side-Channel Attack on a physically isolated (air-gapped) computer. It proves that sensitive data can be "leaked" via electromagnetic emanations. By using a Python-based malware simulation to toggle CPU states, we create On-Off Keying (OOK) modulated radio signals that are intercepted and decoded using Software-Defined Radio (SDR) principles.

**2. Requirements & Installation**
To run this project, you need a Linux environment (Kali Linux recommended) with the following tools installed:
Software Dependencies
Python 3.x: For signal generation.
NumPy: Python library for numerical processing.
GNU Radio Companion (v3.8+): The DSP toolkit used to build the receiver.
xxd: A command-line tool for viewing binary files.
Installation Commands
Run the following in your terminal to ensure everything is ready:
Bash
sudo apt update
sudo apt install gnuradio python3-numpy xxd -y

**3. Project Components**
generate_leak.py: The "Malware" script. It creates airgap_sim.iq, a digital recording of the radio pulses.
AirGap_Decoder.grc: The GNU Radio flowgraph. This is the "brain" of the receiver that cleans the signal and converts it to bits.
decoded_bits.bin: The final output file containing the recovered data.

**4. How to Reproduce**
Generate the Signal: Run the Python script to create the fake radio leak.
Bash
python3 generate_leak.py
Run the Decoder: Open GNU Radio Companion and load AirGap_Decoder.grc.
Click the Green Play Triangle.
Observe the QT GUI Time Sink to see the square waves forming.
Let it run for 10 seconds, then click the Red Stop Square.
Verify the Output: Check the terminal to see the recovered binary data.
Bash
xxd -b decoded_bits.bin | head -n 20
**5. Expected Output**
Visual Output (GNU Radio)
The Time Sink should display a clear "Square Wave." High levels represent a binary 1 (signal present), and low levels represent a binary 0 (silence).

Data Output (Terminal)
The xxd command will show rows of binary bits. A successful recovery looks like this:
00000000: 00000001 00000000 00000001 00000000
This proves the digital signal was correctly reconstructed from the raw IQ radio data.

**6. Conclusion & Defensive Measures**
This project highlights that "Air-Gapping" is a logical security boundary, not a physical one.


Defenses:

Shielding: Use of Faraday cages to block RF emissions.

Jamming: Generating "white noise" to mask secret signals.

Zoning: Keeping high-security machines far away from unvetted radio receivers.
