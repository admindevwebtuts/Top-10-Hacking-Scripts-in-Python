# KillingPythonProcess.py
import os
import signal

def kill_process(pid):
    print(f"Attempting to kill process with PID: {pid}...")

    try:
        os.kill(pid, signal.SIGTERM)
        print(f"Process with PID: {pid} has been terminated.")
    except ProcessLookupError:
        print(f"No running process with PID: {pid}.")

if __name__ == "__main__":
    pid = int(input("Enter the PID of the process to terminate: "))
    kill_process(pid)
