import psutil
import time
import os
import platform
import wmi
import socket

c = wmi.WMI()

def get_network_speed(prev):
    new = psutil.net_io_counters()
    upload = (new.bytes_sent - prev.bytes_sent) / 1024
    download = (new.bytes_recv - prev.bytes_recv) / 1024
    return upload, download, new

def get_local_ip():
    addrs = psutil.net_if_addrs()
    for iface, info in addrs.items():
        for entry in info:
            if entry.family == socket.AF_INET and entry.address != "127.0.0.1":
                return entry.address
    return "N/A"

def get_gpu_info():
    gpus = c.Win32_VideoController()
    if not gpus:
        return None, None
    gpu = gpus[0]
    return gpu.Name, gpu.AdapterRAM

def get_cpu_temp():
    temps = c.Win32_TemperatureProbe()
    if temps:
        return temps[0].CurrentReading
    return None

def monitor():
    prev_net = psutil.net_io_counters()

    while True:
        os.system("cls")

        cpu = psutil.cpu_percent()
        freq = psutil.cpu_freq().current
        cores = psutil.cpu_count()

        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        upload, download, prev_net = get_network_speed(prev_net)

        gpu_name, gpu_mem = get_gpu_info()

        print("=== LIVE SYSTEM MONITOR ===")
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Uptime: {time.strftime('%H:%M:%S', time.gmtime(time.time() - psutil.boot_time()))}")
        print()
        print(f"CPU: {cpu}% | {freq:.0f} MHz | Cores: {cores}")
        print(f"RAM: {ram.percent}% | {ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB")
        print(f"Disk: {disk.percent}%")
        print()
        print(f"Network ↓ {download:.1f} KB/s ↑ {upload:.1f} KB/s")
        print(f"Local IP: {get_local_ip()}")
        print()
        print(f"GPU: {gpu_name}")

        # FIXED GPU MEMORY BLOCK
        if gpu_mem and gpu_mem > 0:
            print(f"GPU Memory: {gpu_mem // (1024**2)} MB")
        else:
            print("GPU Memory: N/A")

        print()
        print("Press CTRL+C to exit")

        time.sleep(1)
