import os
import sys
import signal
import schedule
import time
import threading

def my_job():
    # Lógica de tu tarea o job
    from home.views import thread_processing_students
    thread_processing_students()

def run_schedule(stop_event):
    while not stop_event.is_set():
        schedule.run_pending()
        time.sleep(1)

def handle_interrupt(signum, frame):
    # Maneja la señal de interrupción (Ctrl+C)
    print("Deteniendo el servidor...")

    # Configura la variable de control para detener el job
    stop_event.set()

    # Detén el servidor Django
    sys.exit(0)

if __name__ == '__main__':
    # Configura la variable de control para detener el job
    stop_event = threading.Event()

    # Programa el job antes de ejecutar la aplicación de Django
    schedule.every(1).minutes.do(my_job)

    # Ejecuta el job en un hilo separado
    schedule_thread = threading.Thread(target=run_schedule, args=(stop_event,))
    schedule_thread.start()

    # Registra el manejador de señal para Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)

    # Ejecuta toda la aplicación de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campusVirtual.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
