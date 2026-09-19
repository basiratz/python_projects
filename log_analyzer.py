info_count = 0
warning_count = 0
error_count = 0

errors = []

try:
    with open("robot_log.txt", "r") as file:

        for line in file:
            line.strip()

            if "INFO"  in line:
                info_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

                #getting the actual error form log line
                parts = line.split("ERROR ", 1)
                error_message = parts[1]

                errors.append(error_message)

    print("INFO:", info_count)
    print("WARNING:", warning_count)
    print("ERROR:", error_count)

    print("\nErrors:")

    for error in errors:
        print("-", error)
        
except FileNotFoundError:
    print("Error: robot_log.txt was not found.")