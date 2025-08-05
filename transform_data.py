from datetime import datetime

def transform_weather_data(raw_data):
    if not raw_data or "main" not in raw_data:
        return None
    return {
        "city": raw_data.get("name"),
        "temperature": raw_data["main"].get("temp"),
        "humidity": raw_data["main"].get("humidity"),
        "pressure": raw_data["main"].get("pressure"),
        "weather":raw_data["weather"][0].get("main"),
        "description": raw_data["weather"][0].get("description"),
        "wind_speed": raw_data["wind"].get("speed"),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }