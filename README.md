# AmazingHandAllFingerCheck

A simple Python 3 script that allows all four fingers of the Amazing Hand to be tested simultaneously.

The script operates the Amazing Hand from the following repository:  
https://huggingface.co/blog/pollen-robotics/amazing-hand

**Disclaimer:** This code is NOT an official release from the creators of Amazing Hand (Pollen Robotics). It is an independent implementation.

## How to run the script

1. Assemble all four fingers and connect them to the Waveshare servo bus.
2. Create a Python virtual environment (`venv`).
3. Activate the virtual environment and install the required dependencies:

   `pip install numpy rustypot`

4. Run the script:

   `python3 AmazingHand_FourFingersTest.py`
