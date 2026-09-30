import subprocess
import sys
import time
from pathlib import Path


def launch_streamlit():
    project_root = Path(__file__).resolve().parent
    for port in range(8501, 9001):
        cmd = [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "UI/app.py",
            "--server.headless",
            "true",
            "--server.port",
            str(port),
        ]
        proc = subprocess.Popen(cmd, cwd=str(project_root), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        time.sleep(2)
        if proc.poll() is None:
            print(f"Streamlit app is running on http://localhost:{port}")
            return proc
        output = proc.communicate(timeout=5)[0] if proc.stdout else ""
        if "Port" in output and "not available" in output:
            continue
        print(output)
        return proc
    raise RuntimeError("Unable to start Streamlit. No free port found in range 8501-9000.")


if __name__ == "__main__":
    launch_streamlit()
