import serial
import time

# Replace 'COM3' with the port your Arduino is connected to
arduino_port = '/dev/ttyACM0'
baud_rate = 9600

# Open serial port
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2) # Wait for the serial connection to initialize

try:
    # Continuously take input and send
    while True:
        data_to_send = input()
        arduino.write(data_to_send.encode()) # Convert string to bytes and send
        print(f"Sent: {data_to_send}")

except KeyboardInterrupt:
    # This block will execute when the program is manually stopped (e.g., by pressing Ctrl+C)
    print("Stopping the program...")

finally:
    # Close the serial connection
    arduino.close()
    print("Serial connection closed.")
