# MAST30034 Project 1 README.md
- Name: Un Leng Kam
- Student ID: 1178863

**Research Goal:** My research goal is predict the number high value trips given a location and time.

**Timeline:** The timeline for the research area is 2016 January to 2017 May.

## Dataset
**TLC trip record data:**  https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

**New York City Weather:** https://www.visualcrossing.com/weather/weather-data-services

For the taxi zone data set, used in `visualisation.ipynb` under the file path `../data/taxi_zones/`, please download the dataset from `https://github.com/akiratwang/MAST30034_Python`. Weather dataset was provided to the repository as it requires an account to access the data.




## How to use this Repository
Please run the following files inorder, to ensure correct outputs

1. `download.py`: This downloads the raw data into the `data/raw` directory.
2. `preprocess_1.ipynb`: This notebook details all preprocessing steps for TLC taxi data and outputs it to the `data/curated` directory.
3. `preprocess_2.ipynb`: This notebook details all preprocessing steps for NYC weather data and outputs it to the `data/curated` directory.
4. `feature engineering.ipynb`: This notebook details all feature engineering performed on the TLC taxi data and NYC weather data and outputs it to the `data/curated` directory.
5. `analysis_trip_value.ipynb`: This notebook perform analysis on trip value to define high value trips.
6. `aggregation.ipynb`: This notebook aggregates the data base on time and location and outputs it to the `data/curated` directory.
7. `visualisations.ipynb`: This notebook produces visualisation of attributes of interest and outputs it to `\plots`.
8. `modelling.ipynb`: This notebook perform model training and hyperparameter tunning and outputs visualised predictions to `/plots`
