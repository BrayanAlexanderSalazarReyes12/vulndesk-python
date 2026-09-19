import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
DB_PATH = os.path.join(INSTANCE_DIR, "vulndesk.db")


def get_connection():
    os.makedirs(INSTANCE_DIR, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            full_name TEXT,
            email TEXT,
            role TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            title TEXT,
            owner TEXT,
            priority TEXT
        )
    """)

    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM tickets")

    cursor.executemany(
        """
        INSERT INTO users
        (id, username, password, full_name, email, role)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (1, "admin", "admin123", "Administrador VulnDesk", "admin@lab.local", "ADMIN"),
            (2, "analyst", "analyst123", "Analista Auditor", "analyst@lab.local", "ANALYST"),
            (3, "user", "user123", "Usuario Demo", "user@lab.local", "USER"),
        ],
    )

    cursor.executemany(
        """
        INSERT INTO tickets
        (id, title, owner, priority)
        VALUES (?, ?, ?, ?)
        """,
        [
            (1, "Revisar servidor demo", "ACME", "HIGH"),
            (2, "Validar impresora demo", "PORTLAB", "LOW"),
            (3, "Actualizar inventario demo", "ACME", "MEDIUM"),
        ],
    )

    connection.commit()
    connection.close()
