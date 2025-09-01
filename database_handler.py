# database_handler.py
import sqlite3
from datetime import datetime

DATABASE_NAME = "reports.db"

def init_db():
    """Initializes the database and creates the table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            weather_description TEXT NOT NULL,
            headlines TEXT NOT NULL,
            timestamp DATETIME NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_report(report):
    """Saves a report object to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather_reports (city, temperature, weather_description, headlines, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        report.city,
        report.temperature,
        report.weather_description,
        "\n".join(report.headlines), # Store headlines as a single string
        datetime.now()
    ))
    conn.commit()
    conn.close()
    print(f"Report for {report.city} saved to database.")
