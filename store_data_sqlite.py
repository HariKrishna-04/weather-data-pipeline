import sqlite3

def init_db():
    conn=sqlite3.connect("weather_data.db")
    cursor= conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
                  city TEXT,
                   temperature REAL,
                   humidity INTEGER,
                   pressure INTEGER,
                   weather TEXT,
                   description TEXT,
                   wind_speed REAL,
                   timestamp TEXT 
                   )
    """)
    conn.commit()
    return conn
def insert_weather_record(conn, record):
    cursor=conn.cursor()
    cursor.execute("""
                INSERT INTO weather VALUES (?,?,?,?,?,?,?,?)""",
                (
                    record["city"],
                    record["temperature"],
                    record["humidity"],
                    record["pressure"],
                    record["weather"],
                    record["description"],
                    record["wind_speed"],
                    record["timestamp"],
                ))
    conn.commit()
