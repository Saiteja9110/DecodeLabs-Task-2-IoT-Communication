import random
import time
import csv

# Create CSV file
with open('sensor_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Temperature", "Humidity", "Motion"])

    # Simulate data 10 times
    for i in range(10):
        
        # Generate random values
        temperature = random.randint(25, 35)
        humidity = random.randint(40, 70)
        motion = random.choice(["Detected", "No Motion"])

        # Display values
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Motion:", motion)
        print("------------------------")

        # Store data
        writer.writerow([temperature, humidity, motion])

        # Delay
        time.sleep(2)

print("Sensor data stored in sensor_data.csv")
