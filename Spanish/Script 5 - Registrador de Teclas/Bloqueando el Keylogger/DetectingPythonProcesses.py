# DetectandoProcesosPython.py
import psutil

def detectar_procesos_python():
    print("Detectando procesos en ejecución de Python...\n")

    for proc in psutil.process_iter(['pid', 'name']):
        if 'python' in proc.info['name']:
            print(f"PID: {proc.info['pid']}, Nombre del Proceso: {proc.info['name']}")

if __name__ == "__main__":
    detectar_procesos_python()