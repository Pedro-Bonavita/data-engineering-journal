import requests
import pandas as pd

# API Endpoint for weather forecasting
url = 'https://api.open-meteo.com/v1/forecast'

# Requesting user input for coordinates
latitude = float(input('Enter latitude:'))
longitude = float(input('Enter longitude:'))

# Setting up parameters for a 7=das historical dataset
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": ["temperature_2m", "precipitation"],
    "timezone": "auto",
    "past_days": 7
}

# Fetching data from the API
response = requests.get(url, params=params)

# Checking if the request wass successful (Status Code 200)
if response.status_code ==200:
  # Parsing the response to JSON
  data = response.json()

  # Excracting the hourly dictionary wich contains 'time', 'temperature_2m' and 'precipitation'
  hourly_data = data['hourly']

  # Creating a DataFrame to organize the data into rows and columns
  df = pd.DataFrame({
      "timestamp": hourly_data['time'],
      "temperature_c":hourly_data['temperature_2m'],
      "rain_mm": hourly_data['precipitation']
  })


  # Adding a useful column for analysiss
  df['is_raining'] = df['rain_mm'] > 0

  # Exporting the result to a CSV file (requested)
  df.to_csv('weather_report.csv', index=False)

  print("Data successfully retrieved and saved to 'weather_report.csv'")
  print(df.head(10))  # Display the first few rows for verification
else:
  print(f"Error: Unable to access the API. Status Code: {response.status_code}")