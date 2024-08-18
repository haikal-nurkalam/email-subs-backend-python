import schedule
import time
import subprocess

def job():
    print("Running main.py...")
    subprocess.run(["python3", "main.py"])  # Run the main.py script

# Schedule the job to run every 5 minutes (or choose your desired interval)
schedule.every(5).seconds.do(job)

# Keep the scheduler running
while True:
    schedule.run_pending()
    time.sleep(1)
