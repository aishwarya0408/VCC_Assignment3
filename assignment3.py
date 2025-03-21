import psutil
import time
import requests
import subprocess

# Configuration
CPU_THRESHOLD = 75  # Percentage
MEMORY_THRESHOLD = 75  # Percentage
CHECK_INTERVAL = 10  # Seconds
CLOUD_DEPLOYMENT_SCRIPT = "deploy_to_cloud.sh"  # Placeholder for deployment script

# Function to check resource usage
def check_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return cpu_usage, memory_usage

# Function to trigger auto-scaling
def trigger_auto_scaling():
    print("\n[ALERT] Resource threshold exceeded. Initiating auto-scaling...")
    subprocess.run(["bash", CLOUD_DEPLOYMENT_SCRIPT])

# Monitoring Loop
def monitor_system():
    print("Starting system monitoring...\n")
    while True:
        cpu, memory = check_resources()
        print(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")

        if cpu > CPU_THRESHOLD or memory > MEMORY_THRESHOLD:
            trigger_auto_scaling()
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_system()
