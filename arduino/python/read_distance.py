import serial

arduino = serial.Serial("COM3", 9600, timeout=1)

while True:
    distance = arduino.readline().decode().strip()

    if distance:
        print(f"Distance: {distance} cm")
