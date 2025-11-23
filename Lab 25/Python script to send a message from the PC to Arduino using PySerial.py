import serial
import time

# Set your Arduino's serial port and baud rate
arduino_port = 'COM3'   # Change to your actual port (COM4, COM5 etc.)
baud_rate = 9600

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    time.sleep(2)  # Allow Arduino to reset
    print("LED control started. Press Ctrl+C to stop.")

    while True:
        ser.write(b'ON\n')   # Turn LED on
        print("LED is ON")
        time.sleep(1)

        ser.write(b'OFF\n')  # Turn LED off
        print("LED is OFF")
        time.sleep(1)

except serial.SerialException as e:
    print(f"Serial error: {e}")

except KeyboardInterrupt:
    print("\nLED control stopped.")

finally:
    ser.close()
