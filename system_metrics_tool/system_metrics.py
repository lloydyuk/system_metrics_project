import psutil
import platform
import socket
import argparse
from colorama import Fore, Style, init
import os
from datetime import datetime
import time
import argparse
from system_metrics_tool.monitor import monitor

# Initialise colour support for Windows
init(autoreset=True)

def get_system_info():
    """Collect system information and return it as a dictionary."""
    return {
        "os": f"{platform.system()} {platform.release()}",
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "ip": socket.gethostbyname(socket.gethostname())
    }

def colourise(metric_name, value):
    """Return a coloured string based on thresholds."""
    if metric_name == "cpu":
        if value > 95:
            return Fore.RED + f"{value}% (CRITICAL)"
        elif value > 80:
            return Fore.YELLOW + f"{value}% (High)"
        else:
            return Fore.GREEN + f"{value}%"

    if metric_name == "ram":
        if value > 90:
            return Fore.RED + f"{value}% (CRITICAL)"
        elif value > 75:
            return Fore.YELLOW + f"{value}% (High)"
        else:
            return Fore.GREEN + f"{value}%"

    if metric_name == "disk":
        if value > 95:
            return Fore.RED + f"{value}% (CRITICAL)"
        elif value > 80:
            return Fore.YELLOW + f"{value}% (High)"
        else:
            return Fore.GREEN + f"{value}%"

    return str(value)

def display_system_info(info):
    """Print system information in a readable format with colours."""
    print("=== System Information ===")
    print(f"OS: {info['os']}")
    print(f"CPU Usage: {colourise('cpu', info['cpu'])}")
    print(f"RAM Usage: {colourise('ram', info['ram'])}")
    print(f"Disk Usage: {colourise('disk', info['disk'])}")
    print(f"IP Address: {info['ip']}")

def display_single_metric(info, metric):
    """Print only one metric with colour if applicable."""
    print(f"{metric.upper()}: {colourise(metric, info[metric])}")

def write_log(info):
    """Write system info to a timestamped log file."""
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"logs/{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("=== System Information Log ===\n")
        f.write(f"OS: {info['os']}\n")
        f.write(f"CPU Usage: {info['cpu']}%\n")
        f.write(f"RAM Usage: {info['ram']}%\n")
        f.write(f"Disk Usage: {info['disk']}%\n")
        f.write(f"IP Address: {info['ip']}\n")

    print(f"Log saved to {filename}")

def monitor_system(interval, log_enabled):
    """Continuously monitor system metrics at a set interval."""
    print(f"Monitoring system every {interval} seconds. Press CTRL+C to stop.\n")

    try:
        while True:
            info = get_system_info()
            display_system_info(info)

            if log_enabled:
                write_log(info)

            print("\n---\n")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

def main():
    parser = argparse.ArgumentParser(description="System Information Tool")
    parser.add_argument("--cpu", action="store_true", help="Show CPU usage")
    parser.add_argument("--ram", action="store_true", help="Show RAM usage")
    parser.add_argument("--disk", action="store_true", help="Show Disk usage")
    parser.add_argument("--ip", action="store_true", help="Show IP address")
    parser.add_argument("--all", action="store_true", help="Show all system information")
    parser.add_argument("--log", action="store_true", help="Save output to a log file")
    parser.add_argument("--monitor", action="store_true", help="Monitor system continuously")
    parser.add_argument("--interval", type=int, default=5, help="Interval between checks in seconds")

    args = parser.parse_args()
    info = get_system_info()

    # Monitor mode overrides normal behaviour
    if args.monitor:
        monitor_system(args.interval, args.log)
        return

    if args.log:
        write_log(info)

    if args.all:
        display_system_info(info)
        return

    if args.cpu:
        display_single_metric(info, "cpu")
    if args.ram:
        display_single_metric(info, "ram")
    if args.disk:
        display_single_metric(info, "disk")
    if args.ip:
        display_single_metric(info, "ip")

    if not any(vars(args).values()):
        display_system_info(info)

if __name__ == "__main__":
    main()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--monitor", action="store_true", help="Run live system monitor")
    args = parser.parse_args()

    if args.monitor:
        monitor()
        return

    info = get_system_info()
    print(info)

