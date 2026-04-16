#  Weather Data Extraction - API & Pandas Practice

This project was developed as part of my Data Science bootcamp. It demonstrates the ability to consume real-world data from a REST API and transform it into a structured format for analysis.

## Goal
The objective was to fetch 7 days of historical weather data (Temperature and Precipitation) for a specific location and export it to a CSV file for reporting.

## Tech Stack
- **Python 3.12**
- **Requests Library**: To handle HTTP communication with the Open-Meteo API.
- **Pandas**: To structure raw JSON data into a DataFrame and export it as CSV.

## Key Features
- **Dynamic Input**: Accepts latitude and longitude coordinates from the user.
- **Data Transformation**: Converts raw nested JSON data into a clean, tabular format.
- **Feature Engineering**: Added a boolean column `is_raining` to simplify future analysis.
- **Data Persistence**: Automates the creation of a `.csv` file named `weather_report.csv`.

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install requests pandas`.
3. Run the script: `python weather_data_script.py`.
4. Provide the coordinates when prompted.

## 📊 Sample Output
This is a preview of the data generated in `weather_report.csv`:

| timestamp | temperature_c | rain_mm | is_raining |
| :--- | :--- | :--- | :--- |
| 2026-04-10 00:00 | 21.5 | 0.0 | False |
| 2026-04-10 01:00 | 20.8 | 0.2 | True |
| 2026-04-10 02:00 | 20.1 | 1.5 | True |
| ... | ... | ... | ... |

---
*This activity was completed as a practical requirement for the Generation Brasil Data Science Bootcamp, focusing on API integration and data handling.*