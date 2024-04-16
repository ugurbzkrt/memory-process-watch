import psutil
import subprocess
import time

class JavaProcessMetrics:
    def __init__(self, pid):
        self.pid = pid

    def get_cpu_usage(self):
        process = psutil.Process(self.pid)
        return process.cpu_percent(interval=1)

    def get_memory_usage(self):
        process = psutil.Process(self.pid)
        return process.memory_info().rss / (1024 * 1024)  # RSS bellek kullanımı (MB)

    def get_threads(self):
        process = psutil.Process(self.pid)
        return process.num_threads()

    def dump_heap(self, file_path):
        cmd = f"jmap -dump:live,format=b,file={file_path} {self.pid}"
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    # Java uygulamasının PID'sini belirtin
    java_pid = 12345  # PID numarasını güncelleyin

    metrics = JavaProcessMetrics(java_pid)

    while True:
        cpu_usage = metrics.get_cpu_usage()
        memory_usage = metrics.get_memory_usage()
        threads = metrics.get_threads()

        print(f"CPU Kullanımı: {cpu_usage}%")
        print(f"Bellek Kullanımı: {memory_usage:.2f} MB")
        print(f"Thread Sayısı: {threads}")

        # Heap dump almak için
        heap_dump_file = f"/tmp/heapdump_{int(time.time())}.hprof"
        metrics.dump_heap(heap_dump_file)
        print(f"Heap dump alındı: {heap_dump_file}")

        time.sleep(5)  # 5 saniye bekle


