# DetectingPythonProcesses.py
import psutil

def detect_python_processes():
    print("Detecting running Python processes...\n")

    for proc in psutil.process_iter(['pid', 'name']):
        if 'python' in proc.info['name']:
            print(f"PID: {proc.info['pid']}, Process Name: {proc.info['name']}")

if __name__ == "__main__":
    detect_python_processes()
