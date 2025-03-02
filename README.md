# TTC_delay

## Overview
This project analyzes subway delay data to identify patterns and insights. The analysis includes data loading, cleaning, and visualization of subway performance metrics.

## Installation
Clone this repository:
   ```bash
   git clone https://github.com/JYW5114/TTC_delay.git
   ```


## Usage
Run the Jupyter Notebook to analyze subway delay data:
```bash
jupyter notebook subway_analysis.ipynb
```
Run the Jupyter Notebook to analyze streetcar delay data:
```bash
jupyter notebook ttc_streetcar.ipynb
```
Run the Jupyter Notebook to analyze bus delay data:
```bash
jupyter notebook TTC_Bus_Delays_.ipynb
```

Download the file TTC_Bus_Delays.ipynb, upload it on Google Colab, and run it to access :)

### Data
- **subway-data.csv**: Contains subway delay records with columns like Date, Time, Station, Delay Duration, Line, and Vehicle.
- **subway-delay-codes.csv**: Provides descriptions for delay codes found in the main dataset.
- **bus-data.csv**: Contains records of transit delays by the Bus TTC, including the time of delay, location of the delay-causing, incidents, and many others.

### Key Features
- Data Cleaning & Preparation
- Exploratory Data Analysis (EDA)
- Statistical Analysis & Modeling & Predictions
- Data Visualization using Matplotlib & Seaborn

## Dependencies
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- statsmodels
- io
- ipywidgets
- IPython.display
- google.colab
  
## License
This project is licensed under the MIT License.

## Authors
- Yiwei Jiang
- Anh Dang Phuong
- Shannon Tanoto

# Bus Analysis
From the three visualizations produced from the dataset (bus-data.csv):
(1) "Average Delay Time per Hour of the TTC Bus" shows that the peak delay time of approximately 45 minutes is at 7 AM and hits the lowest average delay time of around 20 minutes at 4 PM. It shows fluctuation in the delay times throughout the day, however, we can see that the TTC Bus experiences longer delays in the first half of the day (before noon) compared to the later half (after noon) 

(2) "Top 20 Locations with most delays" ranks the top 20 TTC Bus stations with the most frequent number of delays in 2024 along with the number of times the TTC Bus got delayed in 2024.

(3) "Average Delay Time in minutes by incident for TTC Bus" indicates the reasons for the TTC Bus delays and also the average delay time caused by it. We can see that diversion creates the longest delay time for TTC Bus

Finally, our predictive model takes in the time and location of planned departure to return a time estimation delay in minutes 

# Street Car Analysis
See notebook 
```bash
jupyter notebook subway_analysis.ipynb
```
# Subway Analysis
See notebook 
```bash
jupyter notebook ttc_streetcar.ipynb
```
