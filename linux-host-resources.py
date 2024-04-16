import psutil
import time

class SystemMetrics:
    def __init__(self):
        pass

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        return {
            "total": mem.total / (1024 * 1024),
            "used": mem.used / (1024 * 1024),
            "free": mem.free / (1024 * 1024),
            "percent": mem.percent
        }

if __name__ == "__main__":
    metrics = SystemMetrics()

    while True:
        cpu_usage = metrics.get_cpu_usage()
        memory_usage = metrics.get_memory_usage()

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Total Memory: {memory_usage['total']:.2f} MB")
        print(f"Used Memory: {memory_usage['used']:.2f} MB")
        print(f"Free Memory: {memory_usage['free']:.2f} MB")
        print(f"Memory Usage: {memory_usage['percent']}%")
        print("-----------------------")

        time.sleep(5)  # Wait for 5 seconds

