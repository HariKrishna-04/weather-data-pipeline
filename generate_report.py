import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_query(query):
    conn=sqlite3.connect("weather_data.db")
    df=pd.read_sql_query(query, conn)
    conn.close()
    return df
if __name__== "__main__":
    df=run_query("""
                SELECT city, AVG(temperature) as Temperature FROM weather
                GROUP BY city;
                 """)
    df.set_index("city", inplace=True)
    df.plot(kind="bar", color="skyblue", title="Average temperature by City")
    plt.ylabel("Temperature")
    plt.xlabel("City")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()