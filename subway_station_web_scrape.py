import pandas as pd
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

# Scrape Wikipedia for Toronto Subway Stations
url = "https://en.wikipedia.org/wiki/List_of_Toronto_subway_stations"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the second table on the page (based on your R script)
tables = soup.find_all("table")
subway_table = pd.read_html(str(tables[1]))[0]  # Convert HTML table to DataFrame

# Prepare station addresses for geocoding
subway_table["fullAddress"] = subway_table["Station"] + " Station, Toronto, Canada"

# Initialize geocoder
geolocator = Nominatim(user_agent="toronto_subway_locator")

# Function to geocode with delay to avoid rate limits
def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return pd.Series([location.latitude, location.longitude])
    except:
        return pd.Series([None, None])

# Apply geocoding
subway_table[["lat", "long"]] = subway_table["fullAddress"].apply(get_coordinates)

# Manually correct some stations' coordinates
manual_fixes = {
    "St. Patrick": (43.6548308, -79.3883485),
    "Highway 407": (43.783215, -79.5237479),
    "Vaughan": (43.7942439, -79.5274867),
    "Ossington": (43.6623565, -79.4263675),
}

for station, (lat, lon) in manual_fixes.items():
    subway_table.loc[subway_table["Station"] == station, ["lat", "long"]] = lat, lon

# Display the cleaned DataFrame
print(subway_table.head())

# Save the cleaned station data for future use
subway_table.to_csv("toronto_subway_stations.csv", index=False)
