# Weather Data Pipeline

A Python-based automated weather data collection and analysis pipeline that fetches weather information from multiple cities, stores it in a SQLite database, and generates visual reports.

## Features

- **Multi-city Weather Data Collection**: Automatically fetches weather data from 5 major cities (Mumbai, London, New York, Berlin, Tokyo)
- **Data Storage**: Stores weather information in a local SQLite database
- **Data Visualization**: Generates bar charts showing average temperature by city
- **Automated Scheduling**: Can be scheduled to run automatically using Windows Task Scheduler
- **Error Handling**: Robust error handling for API requests and data processing

## Tech Stack

- **Python 3.x**
- **Libraries**:
  - `requests` - API calls to OpenWeatherMap
  - `sqlite3` - Database operations
  - `pandas` - Data manipulation and analysis
  - `matplotlib` - Data visualization
  - `datetime` - Timestamp handling

## 📁 Project Structure

```
weather-data-pipeline/
│
├── main.py                 # Main execution script
├── config.py              # Configuration settings (API keys, cities)
├── fetch_weather.py       # Weather API integration
├── transform_data.py      # Data cleaning and transformation
├── store_data_sqlite.py   # Database operations
├── generate_report.py     # Data analysis and visualization
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── weather_data.db       # SQLite database (created after first run)
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-data-pipeline.git
cd weather-data-pipeline
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. API Key Setup
1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Replace the API key in `config.py`:
   ```python
   API_KEY = "your_actual_api_key_here"
   ```

### 4. Run the Pipeline
```bash
python main.py
```

## Usage

### Manual Execution
Run the complete pipeline once:
```bash
python main.py
```

### Generate Reports
Create visualizations from stored data:
```bash
python generate_report.py
```

### Automated Scheduling (Windows)
1. Open **Task Scheduler**
2. Create a new basic task
3. Set trigger (e.g., daily at 9:00 AM)
4. Set action to start a program:
   - **Program**: Path to your Python executable
   - **Arguments**: `"path/to/your/main.py"`
   - **Start in**: Your project directory

## Data Schema

The SQLite database stores weather data with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| city | TEXT | City name |
| temperature | REAL | Temperature in Celsius |
| humidity | INTEGER | Humidity percentage |
| pressure | INTEGER | Atmospheric pressure |
| weather | TEXT | Weather condition |
| description | TEXT | Detailed weather description |
| wind_speed | REAL | Wind speed |
| timestamp | TEXT | Data collection timestamp |

## Configuration

### Adding New Cities
Edit the `CITIES` list in `config.py`:
```python
CITIES = ["Mumbai", "London", "New York", "Berlin", "Tokyo", "Paris", "Sydney"]
```

### Changing Data Collection Frequency
Modify the Task Scheduler settings or use cron jobs on Linux/Mac systems.

## Requirements

Create a `requirements.txt` file with:
```
requests==2.31.0
pandas==2.0.3
matplotlib==3.7.2
```
