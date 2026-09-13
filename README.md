# System Metrics Tool

![Python](https://img.shields.io/badge/Python-3.14.6-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Build Status](https://github.com/lloydyuk/system_metrics_project/actions/workflows/ci.yml/badge.svg)

System Metrics Tool is a lightweight Python command‑line utility that displays live system information in real time.
It provides a clean terminal dashboard showing CPU usage, clock speed, RAM consumption, disk utilisation, network upload/download speeds, GPU details, and system uptime — all refreshed every second.

Designed for simplicity and clarity, the tool runs on Windows and uses psutil and wmi to gather hardware metrics.
Once installed, it can be launched from any terminal using a single command.


Instructions:
1.
Install Python (if you haven’t already)
Prerequisite
The tool requires Python 3.10+ installed on your system.

Download Python from the official website

During installation, tick Add Python to PATH

Verify installation by running python --version in PowerShell

2.
Clone or download the project
Start here
Get the project files onto your machine.

If using Git: git clone https://github.com/lloydyuk/system_metrics_project.git

Or download the ZIP from GitHub and extract it

3.
Install the tool in editable mode
This makes the sysinfo command available everywhere.

Run in PowerShell: pip install -e .

Navigate into the project folder first: cd system_metrics_project

Run the install command

You should see Successfully installed system-metrics-tool

4.
Run the live system monitor
Launch the dashboard from any terminal.

Run: sysinfo --monitor

The screen will refresh every second

Press CTRL + C to exit

You’ll see CPU, RAM, disk, network, GPU, and uptime stats

5.
Update the tool after making changes
Editable mode lets you update the command instantly.

Run again: pip install -e .

Any changes to your Python files will be reflected

No need to uninstall or rebuild the package
