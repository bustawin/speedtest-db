import os

DB_URI = os.getenv(
    "NETWORKY_DATABASE_URI", "postgresql://networky:1234@localhost/networky"
)
