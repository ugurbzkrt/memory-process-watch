import psutil
import subprocess
import time

class JavaProcessMetrics:
    def __init__(self):
        self.pids = self.get_java_pids()

    def get_java_pids(self):
        try:
            output = subprocess.check_output(["jps"]).decode("utf-8")
            java_pids = []
            for line in output.splitlines():
                parts = line.split()
                if len(parts) == 2:
                    pid, name = parts
                    if name.endswith(".jar") or name.endswith(".class"):
                        java_pids.append(int(pid))
            return java_pids
        except FileNotFoundError:
            print("jps command not found. Please make sure Java is installed.")
            exit(1)

    def get_memory_usage(self, pid):
        cmd = f"cat /proc/{pid}/status | grep VmRSS | awk '{{print $2}}'"
        try:
            output = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
            return int(output) / 1024  # Convert to MB
        except subprocess.CalledProcessError:
            print(f"Error getting memory usage for PID {pid}")
            return 0.0

if __name__ == "__main__":
    metrics = JavaProcessMetrics()

    while True:
        for pid in metrics.pids:
            memory_usage = metrics.get_memory_usage(pid)
            print(f"Java Process PID: {pid}")
            print(f"Used Memory: {memory_usage:.2f} MB")
            print("-----------------------")

        time.sleep(5)  # Wait for 5 seconds
