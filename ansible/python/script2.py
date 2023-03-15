import csv
import os
import subprocess
import time

MAINTENANCE_FILE = "/tmp/maintenance.txt"
CSV_FILE = "/tmp/top_process.csv"

def is_top_running():
    """Check if the Top process is running."""
    cmd = ["pgrep", "-f", "top"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return p.returncode == 0

def start_top():
    """Start the Top process."""
    cmd = ["top", "-b"]
    subprocess.Popen(cmd)

def is_maintenance_mode():
    """Check if the maintenance file exists."""
    return os.path.exists(MAINTENANCE_FILE)

def write_csv(date, message):
    """Write a row to the CSV file."""
    with open(CSV_FILE, "a") as f:
        writer = csv.writer(f)
        writer.writerow([date, message])

if __name__ == "__main__":
    start_time = time.time()
    while time.time() - start_time < 300:  # run for 5 minutes
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        if is_top_running():
            message = "Top is running"
        else:
            if not is_maintenance_mode():
                start_top()
            message = "Top was started"
        write_csv(date, message)
        if is_maintenance_mode():
            write_csv(date, "We are under maintenance mode!")
        time.sleep(5)

    # Extract lines with "We are under maintenance mode!"
    with open(CSV_FILE, "r") as f:
        reader = csv.reader(f)
        lines = [line for line in reader if "We are under maintenance mode!" in line[1]]
        count = len(lines)
        print("Found {count} lines with 'We are under maintenance mode!'")
