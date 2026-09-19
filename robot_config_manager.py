import json

def load_config():
    try:
        with open("robot_config.json", "r") as file:
            config = json.load(file)

        return config
    
    except FileNotFoundError:
        print("Error: configuration file not found.")

    except json.JSONDecodeError:
        print("Error: configuration file contains invalid JSON.")
        return None

def display_config(config):
    print("\n--- Robot Configuration ---")

    print("Name:", config["name"])
    print("Wheel radius:", config["wheel_radius"])
    print("Maximum speed:", config["max_speed"])
    print("Sensors:", config["sensors"])
    print("Battery capacity:", config["battery_capacity"])

def save_config(config):
    try:
        with open("robot_config.json", "w") as file:
            json.dump(config, file, indent=4)

        print("Configuration saved successfully.")

    except OSError:
        print("Error: could not save configuration.")

def main():
    config = load_config()

    if config is None:
        return

    display_config(config)

    #Modify configuratioon
    new_speed = float(input("\nEnter new maximum speed: "))

    config["max_speed"] = new_speed

    print("\nUpdated configuration:")
    display_config(config)

    save_config(config)

main()



