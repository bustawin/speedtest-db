import os

DB_URI = os.getenv(
    "NETWORKY_DATABASE_URI", "postgresql://networky:1234@localhost/networky"
)

THREADS = len(os.sched_getaffinity(0))  # Max number of CPUs we can use
SERVERS = [21516]  # Masmovil
