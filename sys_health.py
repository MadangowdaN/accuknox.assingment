import psutil

# Define thresholds
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 80  # Percentage

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_percent}%")
    if cpu_percent > CPU_THRESHOLD:
        print(f"Alert: CPU usage ({cpu_percent}%) exceeds threshold ({CPU_THRESHOLD}%)")

def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    print(f"Memory usage: {memory_percent}%")
    if memory_percent > MEMORY_THRESHOLD:
        print(f"Alert: Memory usage ({memory_percent}%) exceeds threshold ({MEMORY_THRESHOLD}%)")

def check_disk_usage():
    disk_percent = psutil.disk_usage('/').percent
    print(f"Disk usage: {disk_percent}%")
    if disk_percent > DISK_THRESHOLD:
        print(f"Alert: Disk usage ({disk_percent}%) exceeds threshold ({DISK_THRESHOLD}%)")

def check_running_processes():
    processes = psutil.process_iter()
    num_processes = len(list(processes))
    print(f"Number of running processes: {num_processes}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
