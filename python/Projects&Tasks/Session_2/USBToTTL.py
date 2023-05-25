import serial
import csv
import time

# Open the serial port at a baud rate of 9600
ser = serial.Serial('/dev/ttyAMA0', 9600)

# Open the CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(['Data'])

    # Read data from the serial port and write it to the CSV file
    while True:
        data = ser.readline().decode().strip()
        print(data)
        if data:
            writer.writerow([time.time(), data])
            csvfile.flush()

# Close the serial port
ser.close()
