# MatarProcesoPython.py
import os
import signal

def matar_proceso(pid):
    print(f"Intentando matar el proceso con PID: {pid}...")

    try:
        os.kill(pid, signal.SIGTERM)
        print(f"El proceso con PID: {pid} ha sido terminado.")
    except ProcessLookupError:
        print(f"No hay ningún proceso en ejecución con PID: {pid}.")

if __name__ == "__main__":
    pid = int(input("Ingrese el PID del proceso a terminar: "))
    matar_proceso(pid)