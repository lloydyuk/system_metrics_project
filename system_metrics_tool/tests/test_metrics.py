import importlib.util
import sys
import os

project_root = os.path.dirname(os.path.dirname(__file__))
module_path = os.path.join(project_root, "system_metrics.py")

spec = importlib.util.spec_from_file_location("system_metrics", module_path)
system_metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(system_metrics)

get_system_info = system_metrics.get_system_info
colourise = system_metrics.colourise
write_log = system_metrics.write_log

def test_get_system_info_structure():
    info = get_system_info()
    assert isinstance(info, dict)
    assert "cpu" in info
    assert "ram" in info
    assert "disk" in info
    assert "os" in info
    assert "ip" in info

def test_cpu_range():
    info = get_system_info()
    assert 0 <= info["cpu"] <= 100

def test_ram_range():
    info = get_system_info()
    assert 0 <= info["ram"] <= 100

def test_disk_range():
    info = get_system_info()
    assert 0 <= info["disk"] <= 100

def test_colourise_cpu():
    result = colourise("cpu", 50)
    assert "50%" in result

def test_log_file_creation(tmp_path):
    info = get_system_info()

    # Create a temporary logs directory inside pytest's tmp_path
    test_log_dir = tmp_path / "logs"
    os.makedirs(test_log_dir, exist_ok=True)

    # Temporarily switch working directory so write_log writes into tmp_path/logs
    original_dir = os.getcwd()
    os.chdir(tmp_path)

    write_log(info)

    # Switch back to original working directory
    os.chdir(original_dir)

    # Check that a log file was created
    files = list(test_log_dir.glob("*.txt"))
    assert len(files) == 1
