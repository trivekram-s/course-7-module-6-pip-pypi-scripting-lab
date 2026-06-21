from datetime import datetime
import os

def generate_log(data):
    """
    Generate a dated log file from a list of log entries.
    """
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]
    generate_log(sample_data)
