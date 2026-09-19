readings = []

try:
    #read the sensor dat
    with open("sensor_data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            reading = float(line)
            readings.append(reading)

    # Make sure we actually have data
    if len(readings) == 0:
        print("Error: the file contains no sensor readings.")
    else:
        # Ask the user for a threshold
        threshold = float(input("Enter threshold: "))

        #Calculate statistics
        minimum = min(readings)
        maximum = max(readings)
        average = sum(readings)/len(readings)

        above_threshold = [
            reading for reading in readings
            if reading > threshold
        ]

        #store the results in a dictionary
        statistics = {
            "minimum": minimum,
            "maximum": maximum,
            "average": average,
            "above_threshold_count": len(above_threshold)
        }

        #display results
        print("\n--- Sensor Analysis ---")

        
        print("Number of readings:", len(readings))
        print("Minimum:", statistics["minimum"])
        print("Maximum:", statistics["maximum"])
        print("Average:", statistics["average"])

        print("\nReadings above threshold:")
        print(above_threshold)

        print(
            "Number above threshold:",
            statistics["above_threshold_count"]
        )
except FileNotFoundError:
    print("Error: sensor_data.txt was not found.")
except ValueError:
    print("Error: Invalid Numeric data found.")