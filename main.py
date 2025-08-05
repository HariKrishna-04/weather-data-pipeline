from fetch_weather import get_weather_data
from transform_data import transform_weather_data
from config import CITIES
from store_data_sqlite import init_db, insert_weather_record

conn=init_db()

for city in CITIES:

    raw = get_weather_data(city)
    cleaned= transform_weather_data(raw)

    if cleaned:
        insert_weather_record(conn, cleaned)